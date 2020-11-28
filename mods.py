print("cargando...")
#!/usr/bin/env Python 3.6
# -*- coding: UTF-8 -*-


import telegram 
from telegram.utils.helpers import escape_markdown
from telegram.ext import Updater, MessageHandler, CommandHandler, InlineQueryHandler, Filters
import os ,sys ,math ,json ,bs4 ,datetime ,requests ,re ,socket ,pickle
from random import *
from io import *
from time   import sleep
from random import randint


# TOKEN AND INIT CONFIGS
def process(name,names,owner,bot_token):
  updater = Updater(token=bot_token,use_context=True)
  dispatcher = updater.dispatcher
  os.system("clear")
  print("""

  --------« CONSOLE OF THE BOT »--------------

  \033[4;33mWELCOME TO THE BOT :\033[0;m {}

  \033[4;33mTOKEN :\033[0;m {}

  \033[4;33mYOUR NAME :\033[0;m {}

  \033[4;33mYOUR GROUP :\033[0;m {}

  \033[4;33mDEVELOPER  :\033[0;m FLYEAD

  \033[4;33mFOR A OPEN SOURCE WORLD\033[0;m

  \033[4;33mDEBES DE APRETAR CTRL+C PARA SALIR\033[0;m

  --------«------------------------»-----------

  ( EN LA CONSOLA SE VERÁN LOS ERRORES DE SE MOSTRARAN EN TIEMPO REAL )

  """.format(names,bot_token,owner,name))

  #end configs

  # ----------------------------------------------------------------
  # CODIGO ABIERTO PARA IMPORTAR Y/O MODIFICAR
  # USO LIBRE Y A SU PROPIA DISCRECION
  #-----------------------------------------------------------------we
  # LOG V0.0.1+ALPHA by L
  def checksum_mod(card_number):
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1
    for count in range(0, num_digits):
      digit = int(card_number[count])
      if not (( count & 1 ) ^ oddeven ):
        digit = digit * 2
      if digit > 9:
        digit = digit - 9
      sum = sum + digit
    return ( (sum % 10) == 0 )
  class Log():
          def __init__(self, archivo="nombre.txt"):
              self.nombre=archivo
          def write(self, mensaje=""):
              with open(self.nombre,"a+") as f:
                  f.seek(0)
                  data = f.read(100)
                  if len(data) > 0:
                      f.write("\n")
                  f.write(mensaje)
                  f.close()
          def reset(self):
              with open(self.nombre,"w") as f:
                  f.write("")
                  f.close()
          def read(self):
              with open(self.nombre,"r") as f:
                  lineas = f.readlines()
                  f.close()
                  return lineas
  class Tools():
        """
        TOOLS IS BASED IN
        CCTOOLS - Multi Tools of Carding, EDUCATIONAL PURPOSES.
        Copyright (C) 2020  

        DISCLAIMER: This file is for informational and educational purposes only. 
        We are not responsible for any misuse applied to it. All responsibility falls on the user

        ||================================================================================||
        || FRAGMENTS USED FROM https://github.com/Lanniscaf/cctools/blob/master/cctools.py||
        ||================================================================================||

        Adapted BY flyead ALL RIGHTS RESERVED
        """
        def __init__(self):
          self.especialCCG = False
          self.fromFileName = 'binlist.txt'
          super()
        def __cardLuhnChecksumIsValid(self,card_number):
          sum = 0
          num_digits = len(card_number)
          oddeven = num_digits & 1

          for count in range(0, num_digits):
              digit = int(card_number[count])

              if not (( count & 1 ) ^ oddeven ):
                  digit = digit * 2
              if digit > 9:
                  digit = digit - 9

              sum = sum + digit

          return ( (sum % 10) == 0 )
        def __ccgen(self, bin_format):
          permiso = True
          while permiso:
            out_cc = ""
            completo = 0
            #Iteration over the bin
            if(bin_format[:1]=="3"):
                self.especial = True
                for i in range(15):
                    try:
                        if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                            out_cc = out_cc + bin_format[i]
                            continue
                        elif bin_format[i] in ("x", "X" ):
                            out_cc = out_cc + str(randint(0,9))
                            continue
                    except:
                        largo = 13 - len(bin_format)
                        for x in range(largo):
                            bin_format += 'x'
                        out_cc = out_cc + str(randint(0,9))
                    else:
                        pass
                if(completo>=14):
                    return('Favor extrapole el bin')
                    break
                    
            else:    
                self.especial=False
                for i in range(15):
                    try:
                        if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                            out_cc = out_cc + bin_format[i]
                            completo+=1
                            continue
                        elif bin_format[i] in ("x", "X" ):
                            out_cc = out_cc + str(randint(0,9))
                            continue
                        
                    except:
                        largo = 15 - len(bin_format)
                        for x in range(largo):
                            bin_format += 'x'
                        out_cc = out_cc + str(randint(0,9))
                    else:
                        return(False)
                        break
                if(completo>=15):
                    return('Favor extrapole')
            #compare common numbers
            numberC=0
            for i in range(len(bin_format)):
              try:
                if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                    numberC+=1
                    continue
                elif bin_format[i] in ("x", "X" ):
                    continue
              except:
                  return('ERRORFATAL')
            #Generate checksum (last digit) -- IMPLICIT CHECK
            for i in range(10):
                checksum_check = out_cc
                if(bin_format[15:]=="" or bin_format[15:] in ("x","X")):
                    checksum_check = checksum_check + str(i)    
                else:
                    checksum_check = checksum_check + bin_format[15:]
                
                #control numbers common
                respect=0
                if(self.especial):
                  #///
                  #Generate checksum (last digit) -- IMPLICIT CHECK
                  for i in range(10):
                      checksum_check = out_cc
                      checksum_check = checksum_check + str(i)

                      if self.__cardLuhnChecksumIsValid(checksum_check):
                          out_cc = checksum_check
                          break
                      else:
                          checksum_check = out_cc
                  return(checksum_check)
                  #///
                else:

                  for i in range(len(bin_format)):
                    
                    if(bin_format[i]==checksum_check[i]):
                      respect+=1
                    else:
                      continue
                  if (self.__cardLuhnChecksumIsValid(checksum_check) and numberC==respect):
                      out_cc = checksum_check
                      permiso= False
                      break
                  else:
                      checksum_check = out_cc
                    

          return(out_cc)   
        def __ccvgen(self):
          if(self.especial==False):
              ccv = ""
              num = randint(10,999)

              if num < 100:
                  ccv = "0" + str(num)
              else:
                  ccv = str(num)
          else:
              ccv = ""
              num = randint(100,9999)

              if num < 1000:
                  ccv = "0" + str(num)
              else:
                  ccv = str(num)
          
          return(ccv)
        def __dategen(self):
          now = datetime.datetime.now()
          date = ""
          month = str(randint(1, 12))
          if(int(month) < 10):
              month = "0"+month
          current_year = str(now.year)
          year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
          date = month + "|" + year

          return date
        def __monthonly(self):
          month= str(randint(1,12))
          if(int(month) < 10):
              month = "0"+month
          return month
        def __yearonly(self):
          now = datetime.datetime.now()
          date = ""
          current_year = str(now.year)
          year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
          return year
        def generador(self, bins, month=False, year=False, codigocvv=False):
          try:
            if(bins != ''):
              beans = list()
              beans.append(self.regex(bins[0])[0])
              cc_list = list()
              for _ in range(10):
                bin_format = beans[0]
                banIA = self.__ccgen(bin_format)
                if(banIA == 'Favor extrapole el bin'):
                  # //EL BIN NO ESTA EXTRAPOLADO
                  return False

                if(month == False):
                  mes=self.__monthonly()
                elif(month != False):
                  mes=month
                if(year == False):
                  ano=self.__yearonly()
                elif(year != False):
                  ano=year
                if(codigocvv == False):
                  carverificationv=self.__ccvgen()
                elif(codigocvv != False):
                  carverificationv=codigocvv
                
                if(banIA == False):
                  return False
                cc_list.append('{0}|{1}|{2}|{3}'.format(banIA,mes,ano,carverificationv))
              return cc_list

          except:
            return False
        def regex(self, toParse):
          format = r'([A-WY-wy-z]|\s)'
          return re.subn(format, '', toParse)
        def ccgenFromList(self, bins, month=False, year=False, cvv=False):
          try:
            if(type(bins) == type([])):
              i = 0
              for l in bins:
                i += 1
              if i == 1:
                return self.generador(bins)
              # // el usuario entrgo una lista de bins
              beans = list()
              for bin_f in bins:
                scaped = self.regex(bin_f)
                beans.append(scaped)
              cc_list = list()
              for bin_format in beans:
                banIA = self.__ccgen(bin_format[0])
                if(banIA == 'Favor extrapole el bin'):
                  # //EL BIN NO ESTA EXTRAPOLADO
                  return False

                if(month == False):
                  mes=self.__monthonly()
                elif(month != False):
                  mes=month
                if(year == False):
                  ano=self.__yearonly()
                elif(year != False):
                  ano=year
                if(cvv == False):
                  carverificationv=self.__ccvgen()
                elif(cvv != False):
                  carverificationv=cvv
                
                cc_list.append('{0}|{1}|{2}|{3}'.format(banIA,mes,ano,carverificationv))
              return cc_list  

          except:
            return False
        def fromFileList(self):
          log = Log(archivo= self.fromFileName)
          result = self.ccgenFromList(log.read())
          log.reset()
          message = ''
          # formato
          for i in result:
            message += i + '\n'
          log.write(mensaje=message)
          

        try:
          # // al iniciar el archivo intenta buscar si hay una lista de bins para usar
          Tools().fromFileList()
        except:
          pass

  class IbanNew():
  	def __init__(self):
  		self.msg=''
  	def IbanX(self):
  		url='https://api.generadordni.es/v2/bank/account?results=3&bic,iban_formatted,ccc_formatted'
  		response= requests.get(url)
  		if response.status_code==200:
  			response_json=response.json()
  			assd=response_json[0]
  			ccc=assd['ccc']
  			iban=assd['iban']
  			entity=assd['entity']
  			bicss=assd['bic']
  			saol=str(bicss)
  			ccc_1=str(ccc)
  			iban_2=str(iban)
  			entity_3=str(entity)
  			self.msg="""
  *ccc:*

  `{0}`

  *iban:*

  `{1}`

  *entity:*

  `{2}`

  *bic:*

  `{3}`
  """.format(ccc_1,iban_2,entity_3,saol)
  def start(update,context):
    user = update.message.from_user.username
    msg="""
  👑<b>{} BIENVENIDO AL BOT DE {}</b>👑

  <u>PARA VER LOS COMANDOS DEBE DE PONER :</u>

  <b>/help</b>

  ᳆ <b>DEVELOPER :</b> @Flyead ᳇
  ᳆ <b>OWNER OF {} :</b> @{} ᳇
  ᳆ <b>CO-OWNER OF {} :</b> @Lanniscaf ᳇""".format(user,name,name,owner,names)
    update.message.reply_text(msg,parse_mode="HTML")
  def generar(update,context):
  	user = update.message.from_user.username
  	args=context.args
  	msg=args
  	if len(args) > 0:
  		print('bin > '+str(msg[0]))
  		binf = msg
  		obj = Tools()
  		a=obj.ccgenFromList(binf)
  		aa=str(a[0])
  		bb=str(a[1])
  		cc=str(a[2])
  		dd=str(a[3])
  		ee=str(a[4])
  		ff=str(a[5])
  		gg=str(a[6])
  		hh=str(a[7])
  		ii=str(a[8])
  		jj=str(a[9])
  		msg="""
  *cc's generadas : *

  `{}`
  `{}`
  `{}`
  `{}`
  `{}`
  `{}`
  `{}`
  `{}`
  `{}`
  `{}`

  *BY:* `{}`""".format(aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,user)
  	else:
  		msg="*RECUERDE QUE EL COMANDO VA SEGUIDO DE UN BIN {} *".format(user)
  	update.message.reply_text(msg,parse_mode='MarkdownV2')
  def checkbin(update,context):
  	user = update.message.from_user.username
  	args=context.args
  	if len(str(args[0])) >= 6 :
  		args=context.args
  		if len(args) > 0:
  				bin= str(args[0])
  				if len(bin) >= 6:
  					bin= str(bin)
  					try:
  						bin= bin.replace("x","")
  						bin= bin.replace("X","")
  						bin= bin.split("|")[0]
  					except:
  						pass
  					bin = str(re.sub('([a-zA-Z]){1,}', '', bin))
  					lenLuhn=len(str(bin))
  					sinccheck=bin[:16]
  					bin = str(bin)
  					bin = re.sub('([a-zA-Z]){1,}', '', bin)
  					try:
  						unks = 0
  						url='https://lookup.binlist.net/'+str(bin)
  						try:
  							page = requests.get(url)
  							page.raise_for_status()
  						except:
  							return alternateS(bin)
  						page= page.content.decode()
  						dic = json.loads(page)
  						try:
  							luhn = dic['number']['luhn']
  						except:
  							luhn = 'DESCONOCIDO'
  							unks+=1
  						try:
  							luhnLen = dic['number']['length']
  						except:
  							luhnLen = 'DESCONOCIDO'
  							unks+=1
  						brand = dic['scheme']
  						try:
  							brand2 = dic["brand"]
  						except:
  							brand2 = ''
  							unks+=1
  						try:
  							tipe = dic["type"]
  						except:
  							tipe = 'DESCONOCIDO'
  							unks+=1
  						try:
  							prepaid = dic["prepaid"]
  						except:
  							prepaid = 'DESCONOCIDO'
  						country= dic["country"]["name"]
  						try:
  							emoji = dic["country"]["emoji"]
  						except:
  							emoji = ""
  						try:
  							bank = dic["bank"]['name']
  						except:
  							bank = 'DESCONOCIDO'
  							unks+=1
  						try:
  							urlBank = dic["bank"]["url"]
  						except:
  							urlBank = 'DESCONOCIDO'
  							unks+=1
  						try:
  							phoneBank = dic["bank"]["phone"]
  						except:
  							phoneBank = 'DESCONOCIDO'
  							unks+=1
  						try:
  							city = dic["bank"]["city"]
  						except:
  							city = 'DESCONOCIDO'
  							unks+=1
  						#bin,brand,brand2,tipe,prepaid,country,bank,phoneBank,city,urlBank
  						msg = """
  *Valid Bin :*

  `{}`

  *Brand :* 

  `{} - {}`

  *Type:* 

  `{}`

  *Prepaid:* 

  `{}`

  *Country:*

  `{}`

  *Bank:* 

  `{}`

  *Telefono del banco:* 

  `{}`		

  *Ciudad:* 

  `{}`

  *Url del banco:* 

  `{}`

  *CHECKED BY : *`{}` 

  """.format(bin,brand,brand2,tipe,prepaid,country,bank,phoneBank,city,urlBank,user)
  					except:
  						msg="bin invalido"
  				else:
  					msg='bin invalido'
  	else:
  		msg="*RECUERDE QUE DEBE DE INGRESAR UN BIN*"
  	update.message.reply_text(msg,parse_mode='MarkdownV2')
  def find(update,context):
    user = update.message.from_user.username
    args=context.args
    if len(args)>0:
          api = "http://ip-api.com/json/"+str(args[0])
          response=requests.get(api)
          response_json=response.json()
          valida=response_json['status']
          if valida=="success":
              IP=response_json['query']
              ASS=response_json['isp']
              ORG=response_json['org']
              CIUDAD=response_json['city']
              sa=response_json['region']
              pepe=response_json['regionName']
              nose=response_json['lat']
              asd=response_json['lon']
              sss=response_json['timezone']
              pene=response_json['zip']
              paisa=response_json['country']
              asssd=response_json['as']
              msg="""
  *Target:*

  `{}`

  *ISP:*

  `{}`

  *AS:*

  `{}`

  *Organizacion:*

  `{}`

  *Pais:*

  `{}`

  *Ciudad:*

  `{}`

  *Region:*

  `{}`

  *Region nombre:*

  `{}`

  *latitud:*

  `{}`

  *Longitud:*

  `{}`

  *Timezone:*

  `{}`

  *Codigo Postal:*

  `{}`

  BY : `{}`   """.format(IP,ASS,asssd,ORG,paisa,CIUDAD,sa,pepe,nose,asd,sss,pene,user)


          else:
            msg="*IP NO VALIDA*"
    else:
          msg="*IP NO VALIDA*"
    update.message.reply_text(msg,parse_mode='MarkdownV2')
  def extrapolar(update,context):
    user = update.message.from_user.username
    args=context.args
    if len(args)>0:
      if len(args)==1:
        if len(args[0])==16:
          cc1=str(args[0])
          mult1=int(cc1[0])*int(cc1[8])
          mult2=int(cc1[1])*int(cc1[9])
          mult3=int(cc1[2])*int(cc1[10])
          mult4=int(cc1[3])*int(cc1[11])
          mult5=int(cc1[4])*int(cc1[12])
          mult6=int(cc1[5])*int(cc1[13])
          mult7=int(cc1[6])*int(cc1[14])
          mult8=int(cc1[7])*int(cc1[15])
          cc2=str(cc1[0])+str(cc1[1])+str(cc1[2])+str(cc1[3])+str(cc1[4])+str(cc1[5])+str(cc1[6])+str(cc1[7])+str(int(mult1))+str(int(mult2))+str(int(mult3))+str(int(mult4))+str(int(mult5))+str(int(mult6))+str(int(mult7))+str(int(mult8))
          a=0
          asd=list()
          for i in cc1:
            if i == cc2[a]:
              asd.append(i)
            else:
              asd.append("x")
            a+=1
          res_one=str(asd[0])+str(asd[1])+str(asd[2])+str(asd[3])+str(asd[4])+str(asd[5])+str(asd[6])+str(asd[7])+str(asd[8])+str(asd[9])+str(asd[10])+str(asd[11])+str(asd[12])+str(asd[13])+str(asd[14])+str(asd[15])
          mult1=int(cc1[0])*int(cc1[1])
          mult2=int(cc1[1])*int(cc1[2])
          mult3=int(cc1[2])*int(cc1[3])
          mult4=int(cc1[3])*int(cc1[4])
          mult5=int(cc1[4])*int(cc1[5])
          mult6=int(cc1[5])*int(cc1[6])
          mult7=int(cc1[6])*int(cc1[7])
          cc2=str(cc1[0])+str(cc1[1])+str(cc1[2])+str(cc1[3])+str(cc1[4])+str(cc1[5])+str(cc1[6])+str(cc1[7])+str(int(mult1))+str(int(mult2))+str(int(mult3))+str(int(mult4))+str(int(mult5))+str(int(mult6))+str(int(mult7))
          a=0
          osd=list()
          for i in cc1:
            if i == cc2[a]:
              osd.append(i)
            else:
              osd.append("x")
            a+=1
          res_two=str(osd[0])+str(osd[1])+str(osd[2])+str(osd[3])+str(osd[4])+str(osd[5])+str(osd[6])+str(osd[7])+str(osd[8])+str(osd[9])+str(osd[10])+str(osd[11])+str(osd[12])+str(osd[13])+str(osd[14])+str(osd[15])
          msg="""
*CC EXTRAPOLADA CORRECTAMENTE*

*PRIMER RESULTADO :* `{}`

*SEGUNDO RESULTADO :* `{}`

*BY :* `{}`""".format(res_one,res_two,user)
        elif len(args[0])==15:
          cc=str(args[0])
          print(cc)
          mult1=int(cc[0])*int(cc[8])
          mult2=int(cc[1])*int(cc[9])
          mult3=int(cc[2])*int(cc[10])
          mult4=int(cc[3])*int(cc[11])
          mult5=int(cc[4])*int(cc[12])
          mult6=int(cc[5])*int(cc[13])
          mult7=int(cc[13])*int(cc[14])
          ccs=str(cc[0])+str(cc[1])+str(cc[2])+str(cc[3])+str(cc[4])+str(cc[5])+str(int(mult1))+str(int(mult2))+str(int(mult3))+str(int(mult4))+str(int(mult5))+str(int(mult6))+str(int(mult7))
          print(ccs)
          osd=list()
          a=0
          for i in range(0,14):
            if cc[a] == ccs[a]:
              osd.append(cc[a])
            else:
              osd.append("x")
            a+=1
          res=str(osd[0])+str(osd[1])+str(osd[2])+str(osd[3])+str(osd[4])+str(osd[5])+str(osd[6])+str(osd[7])+str(osd[8])+str(osd[9])+str(osd[10])+str(osd[11])+str(osd[12])+str(osd[13])
          mult1=int(cc[0])*int(cc[1])
          mult2=int(cc[1])*int(cc[2])
          mult3=int(cc[2])*int(cc[3])
          mult4=int(cc[3])*int(cc[4])
          mult5=int(cc[4])*int(cc[5])
          mult6=int(cc[5])*int(cc[6])
          mult7=int(cc[6])*int(cc[7])
          ccs=str(cc[0])+str(cc[1])+str(cc[2])+str(cc[3])+str(cc[4])+str(cc[5])+str(int(mult1))+str(int(mult2))+str(int(mult3))+str(int(mult4))+str(int(mult5))+str(int(mult6))+str(int(mult7))
          asd=list()
          a=0
          for i in range(0,15):
            if cc[a] ==ccs[a]:
              asd.append(cc[a])
            else:
              asd.append("x")
            a+=1
          res_two=str(asd[0])+str(asd[1])+str(asd[2])+str(asd[3])+str(asd[4])+str(asd[5])+str(asd[6])+str(asd[7])+str(asd[8])+str(asd[9])+str(asd[10])+str(asd[11])+str(asd[12])+str(asd[13])
          msg="""
*CC EXTRAPOLADA CORRECTAMENTE*

*PRIMER RESULTADO : *`{}`

*SEGUNDO RESULTADO : *`{}`

*BY : *`{}`""".format(res,res_two,user)
          update.message.reply_text(msg,parse_mode='MarkdownV2')
        else:
          msg="*{} RECUERDE QUE DEBE DE METER UNA CC VALIDA*".format(user)
          update.message.reply_text(msg,parse_mode='MarkdownV2')
      elif len(args)==2:
        if len(args[0])==16 and len(args[1])==16:
          cc1=str(args[0])
          cc2=str(args[1])
          suma_1=int(cc1[9])+int(cc1[10])
          suma_2=int(cc2[9])+int(cc2[10])
          div_1=round(int(suma_1)/2)*5
          div_2=round(int(suma_2)/2)*5
          rem=int(div_1)+int(div_2)
          bin_1=str(cc1[0])+str(cc1[1])+str(cc1[2])+str(cc1[3])+str(cc1[4])+str(cc1[5])+str(cc1[6])+str(cc1[7])+str(rem)+'xxxxxx'	
          lista=[]
          lista.append(bin_1)
          obj = Tools()
          a = obj.ccgenFromList(lista)
          lol = str(a[0])
          msg_1=str(lol[0])+str(lol[1])+str(lol[2])+str(lol[3])+str(lol[4])+str(lol[5])+str(lol[6])+'x'+str(lol[8])+str(lol[9])+'xx'+str(lol[12])+str(lol[13])+'x'+str(lol[15])
          mult1=int(cc2[0])*int(cc2[8])
          mult2=int(cc2[1])*int(cc2[9])
          mult3=int(cc2[2])*int(cc2[10])
          mult4=int(cc2[3])*int(cc2[11])
          mult5=int(cc2[4])*int(cc2[12])
          mult6=int(cc2[5])*int(cc2[13])
          mult7=int(cc2[6])*int(cc2[14])
          mult8=int(cc2[7])*int(cc2[15])
          cc=str(cc2[0])+str(cc2[1])+str(cc2[2])+str(cc2[3])+str(cc1[4])+str(cc1[5])+str(cc1[6])+str(cc1[7])+str(int(mult1))+str(int(mult2))+str(int(mult3))+str(int(mult4))+str(int(mult5))+str(int(mult6))+str(int(mult7))+str(int(mult8))
          e=0
          osd=[]
          for i in cc1:
            if i == str(cc[e]):
              osd.append(i)
            else:
              osd.append("x")
            e+=1
          msg_2=str(osd[0])+str(osd[1])+str(osd[2])+str(osd[3])+str(osd[4])+str(osd[5])+str(osd[6])+str(osd[7])+str(osd[8])+str(osd[9])+str(osd[10])+str(osd[11])+str(osd[12])+str(osd[13])+str(osd[14])+str(osd[15])
          mult1=int(cc2[0])*int(cc2[1])
          mult2=int(cc2[1])*int(cc2[2])
          mult3=int(cc2[2])*int(cc2[3])
          mult4=int(cc2[3])*int(cc2[4])
          mult5=int(cc2[4])*int(cc2[5])
          mult6=int(cc2[5])*int(cc2[6])
          mult7=int(cc2[6])*int(cc2[7])
          cc=str(cc2[0])+str(cc2[1])+str(cc2[2])+str(cc2[3])+str(cc2[4])+str(cc2[5])+str(cc2[6])+str(cc2[7])+str(int(mult1))+str(int(mult2))+str(int(mult3))+str(int(mult4))+str(int(mult5))+str(int(mult6))+str(int(mult7))
          o=0
          sd=[]
          for i in cc1:
            if i == str(cc[o]):
              sd.append(i)
            else:
              sd.append("x")
            o+=1
          msg_3=str(sd[0])+str(sd[1])+str(sd[2])+str(sd[3])+str(sd[4])+str(sd[5])+str(sd[6])+str(sd[7])+str(sd[8])+str(sd[9])+str(sd[10])+str(sd[11])+str(sd[12])+str(sd[13])+str(sd[14])+str(sd[15])        
          a=0
          so=list()
          for i in cc1:
            if i ==cc2[a]:
              so.append(i)
            else:
              so.append("x")
          msg_4=str(sd[0])+str(sd[1])+str(sd[2])+str(sd[3])+str(sd[4])+str(sd[5])+str(sd[6])+str(sd[7])+str(sd[8])+str(sd[9])+str(sd[10])+str(sd[11])+str(sd[12])+str(sd[13])+str(sd[14])+str(sd[15])
          msg="""
*EXTRADO DE LAS CCS COMPLETO*

*PRIMER RESULTADO : *`{}`

*SEGUNDO RESULTADO : *`{}`

*TERCER RESULTADO : *`{}`

*CUARTO RESULTADO : *`{}`

BY : {}""".format(msg_1,msg_2,msg_3,msg_4,user)
        elif len(args[0])==14 and len(args[1])==14:
          msg="`{}` *DISCULPE ,AÚN ESTÁ EN DE DESARROLLO*".format(user)
        else:
          msg="`{}` *RECUERDA QUE DEBES DE INGRESAR CC'S VALIDAS*".format(user)
      elif len(args)==3:
        if len(args[0])==16 and len(args[1])==16 and len(args[2])==16:
          msg="`{}` *DISCULPE ,AÚN ESTÁ EN DE DESARROLLO*"
        else:
          msg="`{}` RECUERDA QUE DEBES DE INGRESAR CC'S VALIDAS".format(user)
      elif len(args) > 4:
        msg="`{}` *CANTIDAD NO VALIDA*"
        update.message.reply_text(msg,parse_mode='MarkdownV2')
    else:
      msg="`{}` *RECUERDA QUE EL COMANDO VA ACOMPAÑADO DE UNA O MAS CC'S*".format(user)
    update.message.reply_text(msg,parse_mode='MarkdownV2')
  def info(update,context):
  	user = update.message.from_user.username
  	first_name=update.message.from_user.first_name
  	msg="""
<b>NOMBRE DEL BOT : </b><u><i>{}</i></u>

<b>Version : </b><u><i>BETA</i></u>

<b>OWNER : </b><u><i>{}</i></u>

<b>USER : </b><u><i>{}</i></u>

<b>FIRST NAME : </b><u><i>{}</i></u>

<b>GRACIAS POR USAR EL BOT</b>""".format(names,owner,user,first_name)
  	update.message.reply_text(msg,parse_mode="HTML")
  def crear(update,context):
    user = update.message.from_user.username
    args=context.args
    if len(args)==1:
      v=str(args[0])
      if v.lower()=="iban":
        ibba=IbanNew()
        ibba_1=ibba.IbanX()
        ibba_2=ibba.msg
      elif v.lower()=="bin":
        a=randint(4,5)
        b=randint(4,5)
        c=randint(0,9)
        d=randint(0,9)
        e=randint(0,9)
        f=randint(0,9)
        bin=str(int(a))+str(int(b))+str(int(c))+str(int(d))+str(int(d))+str(int(e))+str(int(f))
        if len(bin) >= 6:
          bin= str(bin)
        try:
          bin= bin.replace("x","")
          bin= bin.replace("X","")
          bin= bin.split("|")[0]
        except:
          pass
        bin = str(re.sub('([a-zA-Z]){1,}', '', bin))
        lenLuhn=len(str(bin))
        sinccheck=bin[:16]
        bin = str(bin)
        bin = re.sub('([a-zA-Z]){1,}', '', bin)
        try:
          unks = 0
          url='https://lookup.binlist.net/'+str(bin)
          try:
            page = requests.get(url)
            page.raise_for_status()
          except:
            return alternateS(bin)
          page= page.content.decode()
          dic = json.loads(page)
          try:
            luhn = dic['number']['luhn']
          except:
            luhn = 'DESCONOCIDO'
            unks+=1
          try:
            luhnLen = dic['number']['length']
          except:
            luhnLen = 'DESCONOCIDO'
            unks+=1
          brand = dic['scheme']
          try:
            brand2 = dic["brand"]
          except:
            brand2 = ''
            unks+=1
          try:
            tipe = dic["type"]
          except:
            tipe = 'DESCONOCIDO'
            unks+=1
          try:
            prepaid = dic["prepaid"]
          except:
            prepaid = 'DESCONOCIDO'
          country= dic["country"]["name"]
          try:
            emoji = dic["country"]["emoji"]
          except:
            emoji = ""
          try:
            bank = dic["bank"]['name']
          except:
            bank = 'DESCONOCIDO'
            unks+=1
          try:
            urlBank = dic["bank"]["url"]
          except:
            urlBank = 'DESCONOCIDO'
            unks+=1
          try:
            phoneBank = dic["bank"]["phone"]
          except:
            phoneBank = 'DESCONOCIDO'
            unks+=1
          try:
            city = dic["bank"]["city"]
          except:
            city = 'DESCONOCIDO'
            unks+=1
          #bin,brand,brand2,tipe,prepaid,country,bank,phoneBank,city,urlBank
          ibba_2 = """
  *Valid Bin :*

  `{}`

  *Brand :* 

  `{} - {}`

  *Type:* 

  `{}`

  *Prepaid:* 

  `{}`

  *Country:*

  `{}`

  *Bank:* 

  `{}`

  *Telefono del banco:* 

  `{}`    

  *Ciudad:* 

  `{}`

  *Url del banco:* 

  `{}`""".format(bin,brand,brand2,tipe,prepaid,country,bank,phoneBank,city,urlBank)
        except:
          ibba_2="*bin invalido*"
      else:
        ibba_2="`{}` LO QUE ME PIDIO ES INVALIDO".format(user)
    elif len(args)==2:
      ibba=IbanNew()
      ibba_1=ibba.IbanX()
      ib=ibba.msg
      a=randint(4,5)
      b=randint(4,5)
      c=randint(0,9)
      d=randint(0,9)
      e=randint(0,9)
      f=randint(0,9)
      bin=str(int(a))+str(int(b))+str(int(c))+str(int(d))+str(int(d))+str(int(e))+str(int(f))
      if len(bin) >= 6:
        bin= str(bin)
      try:
        bin= bin.replace("x","")
        bin= bin.replace("X","")
        bin= bin.split("|")[0]
      except:
        pass
      bin = str(re.sub('([a-zA-Z]){1,}', '', bin))
      lenLuhn=len(str(bin))
      sinccheck=bin[:16]
      bin = str(bin)
      bin = re.sub('([a-zA-Z]){1,}', '', bin)
      try:
        unks = 0
        url='https://lookup.binlist.net/'+str(bin)
        try:
          page = requests.get(url)
          page.raise_for_status()
        except:
          return alternateS(bin)
        page= page.content.decode()
        dic = json.loads(page)
        try:
          luhn = dic['number']['luhn']
        except:
          luhn = 'DESCONOCIDO'
          unks+=1
        try:
          luhnLen = dic['number']['length']
        except:
          luhnLen = 'DESCONOCIDO'
          unks+=1
        brand = dic['scheme']
        try:
          brand2 = dic["brand"]
        except:
          brand2 = ''
          unks+=1
        try:
          tipe = dic["type"]
        except:
          tipe = 'DESCONOCIDO'
          unks+=1
        try:
          prepaid = dic["prepaid"]
        except:
          prepaid = 'DESCONOCIDO'
        country= dic["country"]["name"]
        try:
          emoji = dic["country"]["emoji"]
        except:
          emoji = ""
        try:
          bank = dic["bank"]['name']
        except:
          bank = 'DESCONOCIDO'
          unks+=1
        try:
          urlBank = dic["bank"]["url"]
        except:
          urlBank = 'DESCONOCIDO'
          unks+=1
        try:
          phoneBank = dic["bank"]["phone"]
        except:
          phoneBank = 'DESCONOCIDO'
          unks+=1
        try:
          city = dic["bank"]["city"]
        except:
          city = 'DESCONOCIDO'
          unks+=1
        #bin,brand,brand2,tipe,prepaid,country,bank,phoneBank,city,urlBank
        ib_two = """
    *Valid Bin :*

    `{}`

    *Brand :* 

    `{} - {}`

    *Type:* 

    `{}`

    *Prepaid:* 

    `{}`

    *Country:*

    `{}`

    *Bank:* 

    `{}`

    *Telefono del banco:* 

    `{}`    

    *Ciudad:* 

    `{}`

    *Url del banco:* 

    `{}`

    """.format(bin,brand,brand2,tipe,prepaid,country,bank,phoneBank,city,urlBank)
      except:
        ib_two="*bin invalido*"
      ibba_2="""
  *IBAN CREADO*

  {}

  *BIN CREADO*

  {}

  *BY : *`{}`
  """.format(ib,ib_two,user)
    update.message.reply_text(ibba_2,parse_mode='MarkdownV2')
  def help(update,context):
    user = update.message.from_user.username
    msg="""
  👑<b>COMANDOS</b>

  <u>{} los comandos del bot son los siguientes</u>

  👑PARA CREAR BINS , IBAN O LOS 2 JUNTOS :

  <b>BINS</b>

  - /crear bin

  <b>IBAN</b>

  - /crear iban

  <b>BIN E IBAN</b>

  - /crear iban bin

  👑PARA EXTRAPOLAR :

  - /extrapolar

  <b>( ESTE COMANDO VA ACOMPAÑADO DE LAS CC'S )</b>

  👑PARA GENERAR :

  - /generar

  <b>( ESTE COMANDO VA ACOMPAÑADO DEL BIN )</b>

  👑PARA BUSCAR LA INFORMACION DE UNA DIRECCION IP :

  - /find

  <b>( ESTE COMANDO VA COMPAÑADO DE UNA DIRECCION IP )</b>
  👑PARA CHECKEAR BIN:

  - /checkbin

  👑PARA INFORMACION DEL BOT:

  - /info

  <u>GRACIAS {} POR USAR EL BOT</u>""".format(user,user)
    update.message.reply_text(msg,parse_mode='HTML')
  def extr(update,context):
    user=update.message.from_user.username
    args=context.args
    if len(args) ==2:
      cc=str(args[0])
      bins=list()
      binf=str(args[1])
      bins.append(binf)
      if cc.isdigit()==True:
        if len(cc)==16:
          if binf.isdigit()==False:
            binf = bins
            obj = Tools()
            a=obj.ccgenFromList(binf)
            cc_1=str(a[0][0])+str(a[0][1])+str(a[0][2])+str(a[0][3])+str(a[0][4])+str(a[0][5])+str(a[0][6])+"x"+str(a[0][8])+"x"+str(a[0][10])+"x"+str(cc[12])+str(cc[13])+str(cc[14])+str(cc[15])
            cc_2=str(a[1][0])+str(a[1][1])+str(a[1][2])+str(a[1][3])+str(a[1][4])+str(a[1][5])+str(a[1][6])+"x"+str(a[1][8])+"x"+str(a[1][10])+"x"+str(cc[12])+str(cc[13])+str(cc[14])+str(cc[15])
            new=list()
            new_2=list()
            new.append(cc_1)
            new_2.append(cc_2)
            b=obj.ccgenFromList(new)
            c=obj.ccgenFromList(new_2)
            cc1=round(((int(str(b[0][9]))+int(str(b[0][10])))/2)*5)
            cc2=round(((int(str(c[0][9]))+int(str(c[0][10])))/2)*5)
            final=int(str(cc1))+int(str(cc2))
            res_1=str(b[0][0])+str(b[0][1])+str(b[0][2])+str(b[0][3])+str(b[0][4])+str(b[0][5])+str(b[0][6])+str(b[0][7])+str(int(final))+"xxxxxx"
            res_2=str(c[0][0])+str(c[0][1])+str(c[0][2])+str(c[0][3])+str(c[0][4])+str(c[0][5])+str(c[0][6])+str(c[0][7])+str(int(final))+"xxxxxx"
            msg="""
*CC EXTRAPOLADA CORRECTAMENTE :*

`{}`

`{}`

*BY :* `{}`""".format(res_1,res_2,user)
          else:
            msg="`{}` *recuerda ingresar un bin valido*".format(user)
        else:
          msg="`{}` *recuerda ingresar una cc valida*".format(user)
      else:
        msg="`{}` *recuerda que primero va la cc y luego el bin*".format(user)
    else:
      msg="`{}` *recuerde que este extraoplado se hace con cc y bin*".format(user)
    update.message.reply_text(msg,parse_mode='MarkdownV2')
  def gay(update,context):
    user=update.message.from_user.username
    args=context.args
    valor=randint(0,100)
    if len(args)==0:
      msg="⚠️ @{} es {}%  gay 🏳️‍🌈".format(user,valor)
    else:
      persona=str(args[0])
      msg="⚠️ {} es {}%  gay 🏳️‍🌈".format(persona,valor)
    update.message.reply_text(msg)
  def nepe(update,context):
    user=update.message.from_user.username
    args=context.args
    valor=randint(0,100)
    if len(args)==0:
      msg="⚠️ el pene de @{} es de {}cm 😳".format(user,valor)
    else:
      persona=str(args[0])
      msg="⚠️ el pene de @{} es de {}cm 😳".format(persona,valor)
    update.message.reply_text(msg)
  def WelcomeMSG(update,context):
  	bot=context.bot
  	chatD=update.message.chat_id
  	updateMSG=getattr(update,"message",None)
  	for user in updateMSG.new_chat_members:
  		username=user.first_name
  	bot.sendMessage(
  		chat_id=chatD,
  		parse_mode="MarkdownV2",
  		text="""
*BIENVENIDO* `{}` *TE ESTUVIMOS ESPERANDO CON ANSIAS UWU*""".format(username)
  		)
  dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members,WelcomeMSG))
  dispatcher.add_handler(CommandHandler("nepe",nepe))
  dispatcher.add_handler(CommandHandler("gay",gay))
  dispatcher.add_handler(CommandHandler("extr",extr))
  dispatcher.add_handler(CommandHandler("help",help))
  dispatcher.add_handler(CommandHandler("start",start))
  dispatcher.add_handler(CommandHandler("crear",crear))
  dispatcher.add_handler(CommandHandler("info",info))
  dispatcher.add_handler(CommandHandler("extrapolar",extrapolar))
  dispatcher.add_handler(CommandHandler("find",find))
  dispatcher.add_handler(CommandHandler("checkbin",checkbin))
  dispatcher.add_handler(CommandHandler('generar',generar))
  updater.start_polling()
def guardar(ag,vv):
  file=open("documents/{}.txt".format(vv),"w")
  file.write(ag)
  file.close()
def main():
  group_name=open("documents/name.txt","r")
  group=group_name.readlines()
  group_name.close()
  owner_name=open("documents/owner.txt","r")
  owner=owner_name.readlines()
  owner_name.close()
  bot_name=open("documents/bot.txt","r")
  bot=bot_name.readlines()
  bot_name.close()
  token_val=open("documents/token.txt","r")
  token=token_val.readlines()
  token_val.close()
  if len(group)==0:
    Group=input("\033[4;33mingrese el nombre de su grupo :\033[0;m ")
    guardar(Group,"name")
  else:
    Group=group[0]
  if len(owner)==0:
    Owner=input("\033[4;33mingrese su nombre :\033[0;m ")
    guardar(Owner,"owner")
  else:
    Owner=owner[0]
  if len(bot)==0:
    Bot=input("\033[4;33mingrese el nombre del bot :\033[0;m ")
    guardar(Bot,"bot")
  else:
    Bot=bot[0]
  if len(token)==0:
    Token=input("\033[4;33mingrese el token :\033[0;m ")
    guardar(Token,"token")
  else:
    Token=token[0]
  process(Group,Bot,Owner,Token)
main()
