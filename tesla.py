#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import signal
import subprocess
import unicodedata
import time
import sys
from sys import exit
from random import randint
from DTCScrapper import DTCScrapper
import shlex
import pickle
from datetime import datetime ; from dateutil.relativedelta import * 
import calendar
class agd_entry :
	def __init__(self):
		self.year='16'
		self.mounth ='03'
		self.day ='19'
		self.hour='10'
		self.quoi='rdv'
		self.qui='moi'
		self.ref =''
		self.week = ['lundi','mardi','mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
		self.year = ['janvier','février','mars','avril','mai','juin','juillet','aout','septembre','octobre','novembre','décembre']
	def define(self):
		self.day=raw_input('Quel jour ?')
	def define_auto(self,heure,jour,mois,annee,quoi,qui):
		self.year=annee
		self.mounth =mois
		self.day =jour
		self.hour=heure
		self.quoi=quoi
		self.qui=qui
		self.ref = str(self.year)+str(self.mounth)+str(self.day)+str(self.hour)
	def printref(self):
		return str(self.year)+str(self.mounth)+str(self.day)+str(self.hour)
	def printout(self):
		resume=	';'.join([str(self.year),str(self.mounth),str(self.day),str(self.hour),str(self.quoi),str(self.qui)])	
		return resume
	def presentation(self):
		#print "j'imprime"+resume
		resume = 'Entrée: '+self.ref +' : '+self.quoi+' le '+self.week[int(self.day)]+' '+self.year[int(self.mounth)]+' '+str(self.year)+' à '+str(self.hour)+' heures.'
		return resume
	
class agenda:
	def __init__(self,fichier):
		self.path =fichier
		self.agenda_r =""
		self.list_entry=dict()
	def update(self):
		agenda_r=open(self.path,'r')
		agenda_r.read()
		agenda_r.close()
	def addentry(self,entry):
		self.list_entry[entry.ref]=entry
		return self
	def rmventry(self,ref):
		del self.list_entry[ref]
	def display(self):
		for p in self.list_entry.values():		
			print p.presentation()

	def load(self):
		with open(self.path, 'rb') as fichier_depickler:
			SrPickles=pickle.Unpickler(fichier_depickler)
			return SrPickles.load()
	def save(self):
		with open(self.path, 'wb') as fichier_pickler:
			MrPickles=pickle.Pickler(fichier_pickler)
			MrPickles.dump(self)
			
class Bot():
	
	def __init__(self):
		self.irc_engaged = False 
		self.pathagenda = 'Agenda.agd'
		self.continuer = True
		self.cmd_IRC = 'python /home/compsognatus/ornit.py'
		self.cmd_compress = './machin.sh'
		self.agenda=agenda(self.pathagenda)
		self.newentry=agd_entry()		
		self.week = ['lundi','mardi','mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
		self.week_bonheur  = ['MO','TU','WE','TH','FR','SA','SU']
		self.agenda.load()
		self.etat_ornit = ""
		#self.process_irc = subprocess.Popen(['echo', 'Bonjour Julien, TESLA te salue !'])
	def _close(self):
		Bot().destroy()
	def gogo_irc(self):
		#self.process_irc = subprocess.Popen(['python', 'ornit.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		self.irc_engaged = True 
	def fuite_irc(self):
		os.killpg(os.getpgid(self.process_irc.pid), signal.SIGTERM)
		self.irc_engaged = False 
	def dtc(self):
		# Get the quote number from the arguments
		user_limit = randint(1,17340)
		# Initiate the class
		e = DTCScrapper()
		# Create the url
		url_dtc = "http://danstonchat.com/"+str(user_limit)+".html"
		# Get the results
		result_from_scrapper =  e.main(url_dtc)
		final_quote = ""
		iter = 0
		for a in result_from_scrapper:
		    if iter % 2 == 0 :
			final_quote += a
		    else:
			final_quote += a + "\n"
		    iter += 1
		print final_quote

	def compress(self):
		print 'Bien sûr.'
		if "tous" in self.commande :
			listouille = ['/data/Documents/TeX/These4real/img/ChapterLR/','/data/Documents/TeX/These4real/img/Chapter1/','/data/Documents/TeX/These4real/img/ChapterAnt/']
			for file in listouille : 
				print 'je lance la compression pour'+file
				ind=listouille.index(file)					
				cmd='terminator -x sh -c '+'" cd '+file+';'+'machin.sh; bash"'
				exec ("process_compress"+str(ind)+" = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)") 
		else :
			self.selection_dossier_compression=True	
			
			while self.selection_dossier_compression:
				#if not ('lr' in self.commande or 'ant' in self.commande or '1' in self.commande):

		
				self.dossier = raw_input("De quel dossier il s'agit ?")	
				self.access_file =''
				if ('LR' in self.dossier or 'lr' in self.dossier or 'long' in self.dossier or 'range' in self.dossier):
					self.access_file = '/data/Documents/TeX/These4real/img/ChapterLR/'
				elif ('1' in self.dossier or 'theorie' in self.dossier or 'premier' in self.dossier):
					self.access_file = '/data/Documents/TeX/These4real/img/Chapter1/'
				elif ('ant' in self.dossier ) :
					self.access_file = '/data/Documents/TeX/These4real/img/ChapterAnt/'
				if self.access_file !='' and raw_input(  'on parle bien de : ' + self.access_file + ', okay ?') == 'y':
					self.selection_dossier_compression = False 
					print 'je lance la compression pour'+self.access_file
					cmd ='terminator -x sh -c '+'" cd '+self.access_file+';'+'machin.sh; bash"'
					self.process_compress = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid) 
				#time.sleep(1)
				#os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
	def launch_weekend(self):
		repere=time.localtime().tm_wday
		jour =self.week[repere]
		if jour=='samedi' or jour == 'dimanche' : reponse = 'OUIIIIIIII'
		elif time.localtime().tm_hour>18:
			reponse = 'Il est tard, rentre chez toi, ou va dormir.'
		elif time.localtime().tm_hour<8:
			reponse = 'Il est tôt, profites en pour dormir.'		
		else :
			jourrestant=4-repere
			heurerestant = 18-time.localtime().tm_hour
			reponse = 'Non... Il reste '+str(jourrestant)+' jours et '+str(heurerestant)+ ' heures à tirer.'
		print reponse
	def update(self):
		print 'Igooooor'
		cmd ='terminator -x python igor.py'
		self.process_igor = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
		self.continuer=False 
		print(exit)
	def launch_ardour(self):
		preset=['Proc','R16','MTrack']		
		self.commande = raw_input('Quel preset ? Proc, R16 ou MTrack ?')
		self.commande =int(self.commande)-1		
		cmd ='terminator -x '
		cmd=cmd+'qjackctl --preset '
		cmd=cmd+str(preset[self.commande])
		cmd=cmd+'; Ardour4; 1;'
		self.process_ardour = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
	def capot(self):
		subprocess.call(shlex.split('gedit tesla.py'))
	def launch_process(self,cmd):
		print cmd
	def addentry(self):
		newentry=agd_entry()
		hour=''
		rdv=datetime.now()
		self.choix_jour = False
		quoi = 'rdv'
		qui = ''				
		for d in self.week: 
			if d in self.commande:
				self.choix_jour = True
				now= datetime.now()
				strtest='rdv= now+relativedelta(weekday='
				strtest+=self.week_bonheur[self.week.index(d)]
				strtest+='(+1))'
				exec strtest
				qui = 'moi'
		if '"' in self.commande : 
			self.commande.replace('"',"'")
		if "'" in self.commande :
			quoi = self.commande.split("'")[1]
		if 'heure' in self.commande :
			parse=self.commande.split()
			for p in range(0,len(parse)):
				if 'heure' in parse[p] :hour=str(parse[p-1])
		newentry.define_auto(hour,int(rdv.day),int(rdv.month),int(rdv.year),quoi,qui)
		self.agenda=self.agenda.addentry(newentry) 		
		print 'La liste des rdv est maintenant de :'
		for p in self.agenda.list_entry.keys() : print 'Entrée : '+p+' : '+self.agenda.list_entry[p].presentation()
		del newentry, hour
	def rmventry(self):
		parse = self.commande.split()
		ref = 'caca'
		for p in range(0,len(parse)):
			if 'efface' in parse[p] : ref=parse[p+1]
		try :
			self.agenda.rmventry(ref)
			print "Entrée "+ ref +" supprimée."
		except : print "Aucune entrée à cette référence."
	def launch_test(self) : 
		a= "j'ai'me'les 'bugnes"
		print a.split("'")[1]

	def gestion (self):
			minute=datetime.now().minute
			if minute/5==minute/5. : self.agenda.load()
			#if self.etat_ornit != self.process_irc.stdout():
			#	self.etat_ornit = self.process_irc.stdout()
				#print self.etat_ornit
			self.input = raw_input()
			if self.input =='' or self.input=='encore': self.commande=self.commande
			else : self.commande = str(unicodedata.normalize('NFKD', unicode(self.input,'utf8')).encode('ascii','ignore')).lower() 
			if 'agenda' in self.commande:
				if 'ajoute' in self.commande :
					self.addentry()
				elif 'efface' in self.commande:
					self.rmventry()
			if 'deroule' in self.commande :
				self.agenda.display()
			if 'salut' in self.commande :
				print "salut !"
			if 'sauvegarde' in self.commande :
				self.agenda.save()
			if 'charge' in self.commande :
				self.agenda=self.agenda.load()
			if "irc" in self.commande :
				if  self.irc_engaged == False:
					self.gogo_irc()
				elif 'quit' in self.commande :
					self.fuite_irc() 
			if "quit" in self.commande and not 'irc' in self.commande:
				self.continuer = False	
			if "compresse" in self.commande :
				self.compress()
			if 'repete' in self.commande:
				self.launch_process(" ".join(self.commande.split()[1:]))
			if 'week' in self.commande and 'end' in self.commande and '?' in self.commande : 
				self.launch_weekend()
			if 'dtc' in self.commande : 
				self.dtc()
			if 'actualise' in self.commande : 
				self.update()
			if 'capot' in self.commande : 
				self.capot()
			if 'es' in self.commande and 'la' in self.commande:
				print "Oui oui, pas d'inquiétude."
			if 'test' in self.commande : self.launch_test()
			if "ardour" in self.commande :
				self.launch_ardour()	
	def start(self) :
		while self.continuer :
			try : 
				self.gestion()
			except Exception as erreur:
				print erreur
				ans=raw_input( "Je n'ai pas pu aboutir. Veux tu modifier le programme ?")
				if 'y' in ans :
					self.capot()

if __name__ == "__main__":		
	Bot().start()
