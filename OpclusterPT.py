# -*- coding: utf-8 -*-
#/usr/local/lib/python3.6

#Libraries
import os
import shutil
import re
import spacy
import regex
import string
import codecs
import wikipedia
import collections
import unicodedata
from bs4 import BeautifulSoup
FILE_DIR = os.path.dirname(os.path.abspath(__file__))

#Variables
lista_aspectos = []
grupo = []
busca = []
temp00 = []
nlp_pt = spacy.load('pt_core_news_sm')


#Functions
def extrai_correferencias(diretorio_corp):
	#Variables		
	num_cadeias_new=0
	aux_new = []

	#Reading the output directory files of the CORP  
	relevant_path_new = diretorio_corp 
	included_extenstions_new = ['xml']
	file_names_new = [fn_new for fn_new in os.listdir(relevant_path_new)
		if any(fn_new.endswith(ext_new) for ext_new in included_extenstions_new)]

	#Opening the output directory files of the CORP
	for fil_new in sorted(file_names_new):
		os.chdir(diretorio_corp)
		fil2_new = open(fil_new, encoding='ISO-8859-1')
		corp_new = BeautifulSoup(fil2_new,'lxml')
		
		#You can't remove this aux_new.clear() never
		#aux_new.clear()

		#Get the number of children from each root cadeia tag.
		num_cadeias_new = len(corp_new.cadeias.contents)
		item_cadeias_new = range(num_cadeias_new)
		for c_new in item_cadeias_new:
			if corp_new.cadeias.contents[c_new].name is not None:
				num_cadeias2_new = len(corp_new.cadeias.contents[c_new].contents)
				item_cadeias2_new = range(num_cadeias2_new)
						
				#Figure out the full list of correference chains
				for cc_new in item_cadeias2_new:
					if corp_new.cadeias.contents[c_new].contents[cc_new].name is not None:
						aux_new.append(corp_new.cadeias.contents[c_new].contents[cc_new].get('nucleo').lower())
	return(aux_new)

def busca_giria(item_giria):
        giria1 = []
        giria2 = []
        with codecs.open(os.path.join(FILE_DIR, 'girias1.txt'),'r', encoding='UTF-8') as gir1:
                giria1 = gir1.read().lower().splitlines()
        with codecs.open(os.path.join(FILE_DIR, 'girias2.txt'),'r', encoding='UTF-8') as gir2:
                giria2 = gir2.read().lower().splitlines()
        dic_giria = dict(zip(giria1, giria2))
        dicionario_giria = collections.OrderedDict(sorted(dic_giria.items()))

        for chave_giria, valor_giria in sorted(dicionario_giria.items()):
                if str(chave_giria) == str(item_giria):
                        gir = str(valor_giria)
                        return gir
                else:
                        if valor_giria == str(item_giria):
                                gir = str(chave_giria)
                                return gir


def busca_deverbal(item_deverbal): 
        with open(os.path.join(FILE_DIR, 'deverbais1.txt'), encoding='ISO-8859-1') as d1:
                deverbais1 = d1.read().lower().splitlines()
        with open(os.path.join(FILE_DIR, 'deverbais2.txt'), encoding='ISO-8859-1') as d2:
                deverbais2 = d2.read().lower().splitlines()
        dic1 = dict(zip(deverbais1, deverbais2))
        deb = collections.OrderedDict(sorted(dic1.items()))

        for chave, valor in sorted(deb.items()):
                if str(chave) == str(item_deverbal):
                        deverbal = str(valor)
                        return deverbal
                else:
                        if valor == str(item_deverbal):
                                deverbal = str(chave)
                                return deverbal


def busca_estrangeirismo(item_estrangeiro):
        import string
        with open(os.path.join(FILE_DIR, 'estrangeirismo1.txt'), encoding='ISO-8859-1') as es1:
                estrangeirismo1 = es1.read().lower().splitlines()
        with open(os.path.join(FILE_DIR, 'estrangeirismo2.txt'), encoding='ISO-8859-1') as es2:
                estrangeirismo2 = es2.read().lower().splitlines()
        dic2 = dict(zip(estrangeirismo1, estrangeirismo2))
        est = collections.OrderedDict(sorted(dic2.items()))

        for chave1, valor1 in sorted(est.items()):
                if str(chave1) == str(item_estrangeiro):
                        estrangeirismo = str(valor1)
                        return estrangeirismo
                else:
                        if valor1 == str(item_estrangeiro):
                                estrangeirismo = str(chave1)
                                return estrangeirismo


def busca_diminutivo_aumentativo(item_dimiaum):
        import string
        with open(os.path.join(FILE_DIR, 'diminutivo_aumentativo1.txt'), encoding='ISO-8859-1') as dimia1:
                diminuaumet1 = dimia1.read().lower().splitlines()
        with open(os.path.join(FILE_DIR, 'diminutivo_aumentativo2.txt'), encoding='ISO-8859-1') as dimia2:
                diminuaumet2 = dimia2.read().lower().splitlines()
        dic3 = dict(zip(diminuaumet1, diminuaumet2))
        dimutivo_aumentativo = collections.OrderedDict(sorted(dic3.items()))

        for chave2, valor2 in sorted(dimutivo_aumentativo.items()):
                if str(chave2) == str(item_dimiaum):
                        diau = str(valor2)
                        return diau
                else:
                        if valor2 == str(item_dimiaum):
                                diau = str(chave2)
                                return diau


def busca_no_corp(item_corp, diretorio_xml):
	corref = []
	aux00 = []
	aux01 = []
	aux02 = []
	#Reading the output directory files of the CORP  
	relevant_path = diretorio_xml
	included_extenstions = ['xml']
	file_names = [fn for fn in os.listdir(relevant_path)
		if any(fn.endswith(ext) for ext in included_extenstions)]

	#Opening the output directory files of the CORP
	for fil in sorted(file_names):
		os.chdir(diretorio_xml)
		fil2 = open(fil, encoding='ISO-8859-1')
		corp = BeautifulSoup(fil2,'lxml')
					
		#Get the number of children from each cadeia tag.
		num_cadeias=0
		num_cadeias = len(corp.cadeias.contents)
		item_cadeias = range(num_cadeias)
		for c in item_cadeias:
			if corp.cadeias.contents[c].name is not None:
				num_cadeias2 = len(corp.cadeias.contents[c].contents)
				item_cadeias2 = range(num_cadeias2)
				
				#Não pode tirar essa merda desse clear daqui em nome de jesuis
				aux00.clear()
				
				#Figure out the correference chains
				for cc in item_cadeias2:
					if corp.cadeias.contents[c].contents[cc].name is not None:
						#aux.append(corp.cadeias.contents[c].contents[cc].get('nucleo').lower())
						#Add in corref all correfence chains from directory. However, we need just the correference chains inside the input item.
						aux00.append(corp.cadeias.contents[c].contents[cc].get('nucleo').lower())

						for xxx in aux00:
							if xxx == item_corp:
								aux01 = corp.cadeias.contents[c].name
								
								for cc in item_cadeias2:
									if corp.cadeias.contents[c].contents[cc].name is not None:
										if corp.cadeias.contents[c].name == aux01:
											corref.append(corp.cadeias.contents[c].contents[cc].get('nucleo'))
	return(corref)

def remove_valores_da_lista(the_list, val):
		while val in the_list:
			the_list.remove(val)

def remove_repetidos(lista000):   														
	l = []
	for i1 in lista000:
		if i1 not in l:
			l.append(i1)
	l.sort()
	return l

def intersecao(conjuntoA, conjuntoB):
	inter = []
	for xa in conjuntoA:
		for yb in conjuntoB:
			if xa == yb:
				inter.append(xa)
	return inter

def remove_item(my_list,*args):
    deletar = list(args)
    for item in deletar:
        while item in my_list:
            my_list.remove(item)
    return my_list

def limpar_diretorio(dir_path):
        for filename in os.listdir(os.path.join(dir_path)):
                file_path = os.path.join(dir_path, filename)
                try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                                os.unlink(file_path)
                        elif os.path.isdir(file_path):
                                shutil.rmtree(file_path)
                except Exception as e:
                        print('Failed to delete %s. Reason: %s' % (file_path, e))
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Begin
#-------------------------------------------------------------------------------------------------------------------------------------------------------
def OpCluster_Clusterization(produto):

	#1.0 ASPECT IDENTIFICATION------------------------------------------------------------------------------------------------------------------------------
	#1.1 Call the CORP application to process the input number 1 (txt files directory) 
	CORP_DIR = os.path.join(FILE_DIR, 'CORP')
	opened_directory = os.getcwd()

	#Make sure that the directories "Saida" of the CORP application is clear
	limpar_diretorio(os.path.join(CORP_DIR, 'Saida', 'XML'))

	#Call the Java external application CORP to process the txt files
	os.chdir(CORP_DIR)
	os.system(f'java -Dfile.encoding="ISO-8859-1" -jar {os.path.join(CORP_DIR, "corpMultiThread.jar")}')

	#Variables
	lista_aspectos = []
	busca = []
	temp00 = []
	nlp_pt = spacy.load('pt_core_news_sm')

	#1.2 Extracting aspects from conferences chains
	#Extract the aspects from corrference chains with "NOUN" label
	CORP_OUTPUT_PATH = os.path.join(FILE_DIR, 'CORP', 'Saida', 'XML')
	text_corp = (str(extrai_correferencias(CORP_OUTPUT_PATH)))
	doc = nlp_pt(text_corp)
	for token in doc:
		if token.pos_== 'NOUN':
			corref_item = str(token)
			lista_aspectos.append(corref_item)

	#1.3 Extracting aspects from Wikipedia

	#API Wikipedia
	wikipedia.set_lang("pt") 
	#Turn back only the page on input
	pesq = wikipedia.page(produto) 
	#Save the content of page
	topicos = pesq.content
	#Regex to extrac only the topics of page
	wiki_topicos = re.findall(r'== (.*) ==', topicos)

	#Remove noise inside Wikipedia topics
	for pos, wiki_item in enumerate(wiki_topicos): 
		wiki_item = wiki_item.replace(" ", "_").lower()
		if wiki_item == 'ver_também':
			del(wiki_topicos[pos])
		else:
			lista_aspectos.append(wiki_item)

	#Remove duplicate itens
	lista_aspectos = remove_repetidos(lista_aspectos)

	#2.0 HIERARCHICAL CLUSTERING OF ASPECTS--------------------------------------------------------------------------------------------------------------------
	clustAux = []
	grupo = []
	for aspectoFirst in lista_aspectos:
		#Figure out substring from produto name input by user
		if aspectoFirst.find(produto) != -1:
			clustAux.append(aspectoFirst)
			remove_valores_da_lista(lista_aspectos, aspectoFirst)
	grupo.append((produto, clustAux))


	for aspectoSecond in list(lista_aspectos[:]):
		if aspectoSecond not in lista_aspectos:
			continue 
		#for each iteration of the lista_aspectos, it is necessary to clear the "busca" vector
		busca = []
		busca.append(aspectoSecond)

		if busca_giria(aspectoSecond) is not None:
			busca.append(busca_giria(aspectoSecond))

		if busca_deverbal(aspectoSecond) is not None:
			busca.append(busca_deverbal(aspectoSecond))

		if busca_estrangeirismo(aspectoSecond) is not None:
			busca.append(busca_estrangeirismo(aspectoSecond))

		if busca_diminutivo_aumentativo(aspectoSecond) is not None:
			busca.append(busca_diminutivo_aumentativo(aspectoSecond))

		temp00 = busca_no_corp(aspectoSecond, CORP_OUTPUT_PATH)
		if temp00 is not None:
			for item_temp00 in temp00:
				if item_temp00 in lista_aspectos:
					busca.append(item_temp00)
		
		#Remove duplicate itens
		busca = remove_repetidos(busca)

		clustAux = []
		if busca is not None:
			clustAux = intersecao(busca, lista_aspectos)
			grupo.append((aspectoSecond, clustAux))
			for it_c in clustAux:
				remove_item(lista_aspectos, it_c)

	#Make sure that the directories "Entrada" of the CORP application is clear
	limpar_diretorio(os.path.join(CORP_DIR, 'Entrada'))

	os.chdir(opened_directory)
	return grupo

if __name__ == "__main__":
	result = OpCluster_Clusterization('bolsonaro')
	print(result)
		











