"""Gera bp_modelo_xlsx.json, o molde de formatacao da exportacao do BP em Excel.

Uso:  python3 extrai_modelo_xlsx.py /caminho/BP_QUORUM_Oficial.xlsx
Le a formatacao (estilos, colunas, alturas, agrupamentos, paineis congelados)
das abas Consolidado, Premissas New, Impostos Comun., Impostos Tech e BD Omie
da planilha salva pelo Excel, e grava o molde que o botao "Exportar Excel" do
dashboard usa. Rodar de novo sempre que a formatacao da planilha mudar.
"""
import xml.etree.ElementTree as ET, re, json, sys, zipfile, tempfile, os
_dir = tempfile.mkdtemp()
zipfile.ZipFile(sys.argv[1]).extractall(_dir)
B = _dir + '/'
NS='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
ss=[ ''.join(t.text or '' for t in si.iter(NS+'t')) for si in ET.parse(B+'xl/sharedStrings.xml').getroot()]
def col(c):
    n=0
    for ch in c: n=n*26+ord(ch)-64
    return n
def raw(sheet): return open(B+'xl/worksheets/%s.xml'%sheet,encoding='utf-8').read()
def bloco(txt,tag):
    m=re.search(r'<%s[\s>].*?</%s>|<%s[^>]*/>'%(tag,tag,tag),txt,re.S); return m.group(0) if m else ''
def molde(sheet, maxr, maxc, textos_cols=None, numeros_cols=None):
    t=raw(sheet); root=ET.fromstring(t.encode('utf-8'))
    out={'sheetPr':bloco(t,'sheetPr'),'sheetFormatPr':bloco(t,'sheetFormatPr'),'cols':bloco(t,'cols'),'sheetViews':bloco(t,'sheetViews'),'rows':[]}
    for row in root.find(NS+'sheetData'):
        r=int(row.get('r'))
        if r>maxr: break
        at={k:row.get(k) for k in ('ht','customHeight','outlineLevel','hidden','collapsed','s','customFormat') if row.get(k) is not None}
        est=[0]*(maxc+1); txt={}; num={}
        for c in row:
            ci=col(re.match(r'[A-Z]+',c.get('r')).group(0))
            if ci>maxc: continue
            est[ci]=int(c.get('s') or 0)
            v=c.find(NS+'v'); f=c.find(NS+'f')
            if v is None or v.text is None: continue
            if c.get('t')=='s':
                if textos_cols is None or ci in textos_cols: txt[ci]=ss[int(v.text)]
            elif f is None and numeros_cols and ci in numeros_cols:
                num[ci]=float(v.text)
        runs=[]; ci=1
        while ci<=maxc:
            cj=ci
            while cj+1<=maxc and est[cj+1]==est[ci]: cj+=1
            runs.append([ci,cj,est[ci]]); ci=cj+1
        item={'r':r,'a':at,'s':runs}
        if txt: item['t']=txt
        if num: item['n']=num
        out['rows'].append(item)
    return out
modelo={}
st=open(B+'xl/styles.xml',encoding='utf-8').read()
modelo['styles']=st
modelo['dre']=molde('sheet1',322,47,textos_cols={2,3,5,47,43,44,45})
modelo['premissas']=molde('sheet4',13,64)
modelo['impCom']=molde('sheet5',99,24,numeros_cols={21,22,23,24})
modelo['impTech']=molde('sheet6',99,24,numeros_cols={21,22,23,24})
bd=raw('sheet8'); modelo['bd']={'sheetPr':bloco(bd,'sheetPr'),'sheetFormatPr':bloco(bd,'sheetFormatPr'),'cols':bloco(bd,'cols'),'sheetViews':bloco(bd,'sheetViews')}
saida=os.path.join(os.path.dirname(os.path.abspath(__file__)),'bp_modelo_xlsx.json')
json.dump(modelo,open(saida,'w'),ensure_ascii=False,separators=(',',':'))
print('molde gravado em',saida,'-',os.path.getsize(saida)//1024,'KB')
