from django.shortcuts import render, redirect
import os
import zipfile
import yagmail
import requests
from PIL import Image
from io import BytesIO
import json
from pprint import pprint
import pandas as pd
import ast
import shutil
import sys
import os
import datetime
import random
import string
import openpyxl
import os
import datetime
import random
import string
from django.shortcuts import render, redirect
from twocaptcha import TwoCaptcha

def home(request):
    if request.method == 'POST':
          userid = request.POST['user_name']
          pwd = request.POST['password']

          def login(userid, pwd):
               print("############################# Started Def Login Line 25")
               print("line - 24")
               url = "https://static.gst.gov.in/uiassets/css/fonts/minified/FontAwesome.woff2?v=4.7.0"

               headers = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Host": "static.gst.gov.in",
                    "Origin": "services.gst.gov.in",
                    "Referer": "https://static.gst.gov.in/uiassets/css/fwk/fa-bootstrap1.0.css",
                    "Sec-Fetch-Dest": "document",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Site": "none",
                    "Sec-Fetch-User": "?1",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\""
               }
               print(pwd)
               p_cookie = {
                    "Lang": "en"
               }
               cookies=p_cookie
               
               response = requests.get(url, headers=headers, cookies=cookies)
               print("St1")
               # Print the response status code and content
               print(f"Status Code: {response.status_code}")
               received_cookie = response.cookies.get_dict()
               ##    print("Response Cookies : ", received_cookie)
               p_cookie = cookie_update(p_cookie, received_cookie)
               ##    print("Updated Cookie : ", p_cookie)
               ##    print("Response : \n",response.text)
               ##    print("#################################################################################################################################")
               ##################################################################################################################################################################################
               ##################################################################################################################################################################################

               url = "https://services.gst.gov.in"
               ##url = "https://services.gst.gov.in/pages/services/userlogin.html"

               headers = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Host": "services.gst.gov.in",
                    "Pragma": "no-cache",
                    "Sec-Fetch-Dest": "document",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Site": "none",
                    "Sec-Fetch-User": "?1",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\""
               }

               cookies=p_cookie
               response = requests.get(url, headers=headers, cookies=cookies)

               ##    print(f"Status Code: {response.status_code}")
               received_cookie = response.cookies.get_dict()
               ##    print("Response Cookies : ", received_cookie)
               p_cookie = cookie_update(p_cookie, received_cookie)
               ##    print("Updated Cookie : ", p_cookie)
               ##    print("Response : \n",response.text)
               ##    print("#################################################################################################################################")
               ##################################################################################################################################################################################
               ##################################################################################################################################################################################
               print("line - 93")
               # Now we have the cookies which will help us to go and login
               url = "https://services.gst.gov.in/services/api/ustatus"

               headers = {
               ##    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
               ##    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
               ##    "Cookie": f"TS01b8883c={cookies_TS01b8883c['TS01b8883c']};ak_bmsc={cookies_ak_bmsc['ak_bmsc']}",
                    "Host": "services.gst.gov.in",
                    "Pragma": "no-cache",
                    "Referer": "https://services.gst.gov.in/services/login",
                    "Sec-Fetch-Dest": "image",
                    "Sec-Fetch-Mode": "no-cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
               }

               cookies=p_cookie
               response = requests.get(url, headers=headers, cookies=cookies)

               ##    print(f"Status Code: {response.status_code}")
               received_cookie = response.cookies.get_dict()
               ##    print("Response Cookies : ", received_cookie)
               p_cookie = cookie_update(p_cookie, received_cookie)
               ##    print("Updated Cookie : ", p_cookie)
               ##    print("#################################################################################################################################")
               ##    print("Response : \n",response.text)
               ##################################################################################################################################################################################
               ##################################################################################################################################################################################
               print("line - 128")
               # Now we have the cookies which will help us to go and login
               url = "https://services.gst.gov.in/services/captcha"

               headers = {
                    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
               ##    "Cookie": f"TS01b8883c={cookies_TS01b8883c['TS01b8883c']};ak_bmsc={cookies_ak_bmsc['ak_bmsc']}",
                    "Host": "services.gst.gov.in",
                    "Pragma": "no-cache",
                    "Referer": "https://services.gst.gov.in/services/login",
                    "Sec-Fetch-Dest": "image",
                    "Sec-Fetch-Mode": "no-cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
               }
               print("line - 150")
               cookies=p_cookie
               response = requests.get(url, headers=headers, cookies=cookies)

               ##    print(f"Status Code: {response.status_code}")
               received_cookie = response.cookies.get_dict()
               ##    print("Response Cookies : ", received_cookie)
               p_cookie = cookie_update(p_cookie, received_cookie)
               ##    print("Updated Cookie : ", p_cookie)

               if response.status_code == 200:
                    # Assuming the content is an image
                    image = Image.open(BytesIO(response.content))

                    # Save the image as a PNG file
                    print("############################################ Call create_unique_folder2() Line 173 ")
                    unique_folder = create_unique_folder2()
                    print(unique_folder)
                    
                    image.save(unique_folder + "\\" + "captcha.png", format="PNG")
                    print("Image saved successfully in the folder " + unique_folder )
                    
                    captchaCode = Captchaconvert(unique_folder)
                    print("############################################ Call Captchaconvert(unique_folder) Line 181 ")
                    image_path = os.path.join("GSTDEMO" + unique_folder, "captcha.png")
                    print("Image saved successfully as captcha.png")
                    print("################################## Line 184")
                    # Define the new file name
                    '''
                    new_image_path = os.path.join(unique_folder, captchaCode +".png")
                    new_image_path2 = os.path.join("Image_dump",captchaCode +".png")
                    print("Old Image path is :", new_image_path)
                    print("################################## Line 189")
                    print("New Image path is :", new_image_path2)
                    print("########################################## Line 189")
                    # Rename the files
                    print("################################## Line 192")
                    os.rename(image_path, new_image_path2)

                    shutil.move(new_image_path, new_image_path2)
                    
                    print("File Renamed successfully")
                    print(captchaCode)
                    '''
                    
               else:
                    print(f"Failed to retrieve captcha image. Status code: {response.status_code}")
               print("line - 169")
               ##print("Response : \n",response.text)
               print("#################################################################################################################################")
               ##################################################################################################################################################################################
               ##################################################################################################################################################################################

               # captchaCode = input("Please decode the captcha :")

               print("line - 177")
               #print (p_cookie)
               print("line - 179")
               print("######################################################################## End of Login Line 210")
               
               return (p_cookie, captchaCode)

          def complete_login(userid,pwd,captchaCode,p_cookie):
               print("################################# Startedcomplete_login(userid,pwd,captchaCode,p_cookie) Line 259")
               url = "https://services.gst.gov.in/services/authenticate"
               print("line - 261")
               headers = {
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json;charset=UTF-8",
                    "Host": "services.gst.gov.in",
                    "Origin": "https://services.gst.gov.in",
                    "Pragma": "no-cache",
                    "Referer": "https://services.gst.gov.in/services/login",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\""
               }

               # Replace this with the actual JSON payload
               payload = {
                    "username": userid,
                    "password": pwd,
                    "captcha": captchaCode,
                    "mFP": "{\"VERSION\":\"2.1\",\"MFP\":{\"Browser\":{\"UserAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36\",\"Vendor\":\"Google Inc.\",\"VendorSubID\":\"\",\"BuildID\":\"20030107\",\"CookieEnabled\":true},\"IEPlugins\":{},\"NetscapePlugins\":{\"PDF Viewer\":\"\",\"Chrome PDF Viewer\":\"\",\"Chromium PDF Viewer\":\"\",\"Microsoft Edge PDF Viewer\":\"\",\"WebKit built-in PDF\":\"\"},\"Screen\":{\"FullHeight\":864,\"AvlHeight\":816,\"FullWidth\":1536,\"AvlWidth\":1536,\"ColorDepth\":24,\"PixelDepth\":24},\"System\":{\"Platform\":\"Win32\",\"systemLanguage\":\"en-IN\",\"Timezone\":-330}},\"ExternalIP\":\"\",\"MESC\":{\"mesc\":\"mi=2;cd=150;id=30;mesc=757210;mesc=1041587\"}}",
                    "deviceID": None,
                    "type": "username"
               }
               print("line - 291")
               cookies=p_cookie
               ##response = requests.get(url, headers=headers, cookies=cookies)
               
               response = requests.post(url, headers=headers, json=payload, cookies=cookies)

               ##    print(f"Status Code: {response.status_code}")
               received_cookie = response.cookies.get_dict()
               ##    print("Response Cookies : ", received_cookie)
               p_cookie = cookie_update(p_cookie, received_cookie)
               ##    print("Updated Cookie : ", p_cookie)
               ##    print("Response : \n",response.text)
               ##    print("#################################################################################################################################")
               ##################################################################################################################################################################################
               ##################################################################################################################################################################################

               url = "https://services.gst.gov.in/pages/services/data/corbustype.json"

               headers = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
               ##    "Cookie": "Lang=en",
                    "Host": "services.gst.gov.in",
                    "Pragma": "no-cache",
                    "Sec-Fetch-Dest": "document",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Site": "none",
                    "Sec-Fetch-User": "?1",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\""
               }
               print("Ln 328")
               # Add code to remove captcha_cookie
               p_cookie.pop("CaptchaCookie", None)
               cookies=p_cookie
               response = requests.get(url, headers=headers, cookies=cookies)

               print(f"Status Code: {response.status_code}")
               received_cookie = response.cookies.get_dict()
               #print("Response Cookies : ", received_cookie)
               p_cookie = cookie_update(p_cookie, received_cookie)
               # print("Updated Cookie : ", p_cookie)
               #print("Response : \n",response.text)

               print("#################################################################################################################################")
               ##################################################################################################################################################################################
               ##################################################################################################################################################################################

               url = "https://services.gst.gov.in/services/api/ustatus"
               ##  print("Hitting : https://services.gst.gov.in/services/api/ustatus")

               cookies=p_cookie
               response = requests.get(url, headers=headers, cookies=cookies)

               print(f"Status Code: {response.status_code}")
               received_cookie = response.cookies.get_dict()
               ##  print("Response Cookies : ", received_cookie)
               p_cookie = cookie_update(p_cookie, received_cookie)
               ##  print("Updated Cookie : ", p_cookie)
               #print("Response : \n",response.text)
               datactype = response.json()

               # Extract the value of bname

               bname = datactype.get("bname")
               gstin = datactype.get("gstin")
               print("################################# The extracted Data are as follows:", bname, gstin)
               ##    print("#################################################################################################################################")
               ##################################################################################################################################################################################
               ##################################################################################################################################################################################
               print("Ln 366")
               folder_path = create_unique_folder(gstin)
               url = "https://services.gst.gov.in/services2/auth/web/gta/decldtls/getNewTpGTADtls"

               headers = {
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Host": "services.gst.gov.in",
                    "Pragma": "no-cache",
                    "Referer": "https://services.gst.gov.in/services/auth/fowelcome",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "at": "c3f7df3809a54ccfaad2f08dd55b689f",
                    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
               }
               print("Ln 316")
               cookies=p_cookie
               response = requests.get(url, headers=headers, cookies=cookies)

               #print(f"Status Code: {response.status_code}")
               received_cookie = response.cookies.get_dict()
               ##    print("Response Cookies : ", received_cookie)
               p_cookie = cookie_update(p_cookie, received_cookie)
               ##    print("Updated Cookie : ", p_cookie)
               #print("Response : \n",response.text)
               ##    print("#################################################################################################################################")
               ##################################################################################################################################################################################
               ##################################################################################################################################################################################

               url = "https://services.gst.gov.in/returns/auth/api/filingsnapshot"

               headers = {
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Host": "services.gst.gov.in",
                    "Pragma": "no-cache",
                    "Referer": "https://services.gst.gov.in/services/auth/fowelcome",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "at": "c3f7df3809a54ccfaad2f08dd55b689f",
                    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
               }
               print("Ln 350")
               cookies=p_cookie
               response = requests.get(url, headers=headers, cookies=cookies)

               ##    print(f"Status Code: {response.status_code}")
               print("Ln 388 Updated the Noties.... " + str(url))
               received_cookie = response.cookies.get_dict()
               ##    print("Response Cookies : ", received_cookie)
               p_cookie = cookie_update(p_cookie, received_cookie)
               ##    print("Updated Cookie : ", p_cookie)
               #print("Response : \n",response.text)
               ##    print("#################################################################################################################################")
               ##################################################################################################################################################################################
               ##################################################################################################################################################################################

               print("########################################### Started At Line 398")
               #GET 	https://return.gst.gov.in/returns/auth/api/gstr3b/summary?rtn_prd=042024
               url="https://services.gst.gov.in/services/auth/api/get/notices"

               headers = {
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json",
                    "Host": "services.gst.gov.in",
                    "Origin": "https://services.gst.gov.in",
                    "Referer": "https://services.gst.gov.in",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
               }

               payload =  {"onLoad":True}

               cookies=p_cookie
               response = requests.post(url, headers=headers, cookies=cookies, json=payload)

               print("Ln 427 Updated the Noties.... " + str(url))
               ##    print(f"Status Code: {response.status_code}")
               received_cookie = response.cookies.get_dict()
               ##    print("Response Cookies : ", received_cookie)
               p_cookie = cookie_update(p_cookie, received_cookie)
               ##    print("Updated Cookie : ", p_cookie)
               #print("Response : \n",response.text)
               ##    print("#################################################################################################################################")

               response_data = response.json()

               current_directory1 = os.path.join("C:/Users/RAMOFFICE3/OneDrive/Desktop/Manam_Final/Manam_Final/OutputFile/" , folder_path)   
               
               file_path = current_directory1 + "\\" + "Notices-" + bname + "_" + gstin + "__________" + ".json"
               #file_extension = "____.json"
               #file_path = os.path.join(current_directory1, folder_path) + file_extension
                         
                         #ZipFile.write(file_path)
                    # re = response.to_dict()
               # Save the response message as a JSON file
               with open(file_path, 'w') as json_file:
                    json.dump(response_data, json_file)

               # Load the JSON file
               #file_path = 'C:\\python\\project x\\20240617_184108-33AAYCS3291C2Z3-MLSXh\\Notices-SRI VELAVAN MOTORS PRIVATE LIMITED_33AAYCS3291C2Z3_.json'

               # Convert JSON data to a DataFrame
               df = pd.json_normalize(response_data)
               print("Line 457................." , df.head(5))
               # Save DataFrame to Excel
               output_file = current_directory1 + "\\" + "\\notices_data.csv"
               df.to_csv(output_file, index=False)

               print("###################################### all Basic Notices Saved")
               #file_path = current_directory1 + "\\" + folder_path +"\\"+ "GSTR3B-" + bname+ "_" + gstin + "_" + str(x)  + ".json"
                    #ZipFile.write(file_path)
               # re = response.to_dict()
               # Save the response message as a JSON file
               #with open(file_path, 'w') as json_file:
                    #   json.dump(response_data, json_file)
               #print("val of X ##############################" + str(x))
                    #x += 1 
               url = "https://services.gst.gov.in/services/api/ustatus"

               headers = {
               ##    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
               ##    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
               ##    "Cookie": f"TS01b8883c={cookies_TS01b8883c['TS01b8883c']};ak_bmsc={cookies_ak_bmsc['ak_bmsc']}",
                    "Host": "services.gst.gov.in",
                    "Pragma": "no-cache",
                    "Referer": "https://services.gst.gov.in",
                    "Sec-Fetch-Dest": "image",
                    "Sec-Fetch-Mode": "no-cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
               }

               cookies=p_cookie
               response = requests.get(url, headers=headers, cookies=cookies)

               print(f"Status Code.............................. Ustatus............: {response.status_code}")
               received_cookie = response.cookies.get_dict()
               ##    print("Response Cookies : ", received_cookie)
               p_cookie = cookie_update(p_cookie, received_cookie)
               
               url="https://services.gst.gov.in/litserv/auth/api/case/task/get"

               headers = {
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json",
                    "Host": "services.gst.gov.in",
                    "Origin": "https://services.gst.gov.in",
                    "Referer": "https://services.gst.gov.in/litserv/auth/viewadnlntcord",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
               }

               payload =  {"gstIn":gstin}

               cookies=p_cookie
               response = requests.post(url, headers=headers, cookies=cookies, json=payload)

               #print("Ln 512 Updated the additional Notices.... " + str(url))
               ##    print(f"Status Code: {response.status_code}")
               received_cookie = response.cookies.get_dict()
               ##    print("Response Cookies : ", received_cookie)
               p_cookie = cookie_update(p_cookie, received_cookie)
               ##    print("Updated Cookie : ", p_cookie)
               #print("Response : \n",response.text)   
               response_data = response.json()

               #current_directory1 = os.getcwd() 
               
               current_directory1 = "C:/Users/RAMOFFICE3/OneDrive/Desktop/Manam_Final/Manam_Final/OutputFile/"

               file_path = current_directory1 + "\\" + folder_path +"\\"+ "Addl Notices-" + bname+ "_" + gstin + "_" + ".json"
               #file_path = folder_path +"\\"+ "OutputFile" +"\\"+ "Addl Notices-" + bname+ "_" + gstin + "_" + ".json"
               
                         
                         #ZipFile.write(file_path)
                    # re = response.to_dict()
               # Save the response message as a JSON file
               with open(file_path, 'w') as json_file:
                    json.dump(response_data, json_file)
                    # Convert JSON data to a DataFrame
               df = pd.json_normalize(response_data)
               
               print("The filtered notices are here ", df.head())

               # Save DataFrame to Excel
               output_file = current_directory1 + "\\" + folder_path + "\\Addl _notices_data.csv"
               output_file_te = current_directory1 + "\\" + folder_path + "\\Det_Addl _notices_data.csv"
               df.to_csv(output_file, index=False)
               print("###################################### all Additional Notices Saved")
               df_reduced = df[['caseTaskId', 'caseTpeCd', 'caseId', 'gstIn']]
               df_reduced.to_csv(output_file_te , index=True)
               print("################################### Working on with detailed iteration of rows")
               print("The filtered and reduced  notices are here ", df_reduced.head())
               for index, row in df_reduced.iterrows():
                    #print(f"Processing caseTaskId: {row['caseTaskId']}, ARN: {row['arn']}, Case Type: {row['caseTpeCd']}, Case ID: {row['caseId']}")
                    payload = {
                              "caseId":row['caseId'],
                              "gstid":gstin,
                              "caseTypeCd":row['caseTpeCd']
                              
                         }
                    print("The updated iterated payload is here ", payload)

               headers = {
               ##    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
               ##    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
               ##    "Cookie": f"TS01b8883c={cookies_TS01b8883c['TS01b8883c']};ak_bmsc={cookies_ak_bmsc['ak_bmsc']}",
                    #"Host": "services.gst.gov.in",
                    "Pragma": "no-cache",
                    "Referer": "https://services.gst.gov.in",
                    "Sec-Fetch-Dest": "image",
                    "Sec-Fetch-Mode": "no-cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
               }


               
               url = "https://services.gst.gov.in/pages/common/header.html"
               cookies=p_cookie
               response = requests.get(url, headers=headers, cookies=cookies)
               print("Ln 594 Updated the Noties.... " + str(url))
               print(f"Status Code........................... common/header.html  : {response.status_code}")
               received_cookie = response.cookies.get_dict()
               ##    print("Response Cookies : ", received_cookie)
               p_cookie = cookie_update(p_cookie, received_cookie)
               
               url = "https://services.gst.gov.in/pages/common/menu.html"
               cookies=p_cookie
               response = requests.get(url, headers=headers, cookies=cookies)
               print("Ln 594 Updated the Noties.... " + str(url))
               print(f"Status Code........................... /common/menu.html : {response.status_code}")
               received_cookie = response.cookies.get_dict()
               ##    print("Response Cookies : ", received_cookie)
               p_cookie = cookie_update(p_cookie, received_cookie)
               
               url = "https://services.gst.gov.in/pages/common/footer.html"
               cookies=p_cookie
               response = requests.get(url, headers=headers, cookies=cookies)
               print("Ln 594 Updated the Noties.... " + str(url))
               print(f"Status Code...........................s/common/footer.html : {response.status_code}")
               received_cookie = response.cookies.get_dict()
               ##    print("Response Cookies : ", received_cookie)
               p_cookie = cookie_update(p_cookie, received_cookie)
               
               url = "https://services.gst.gov.in/pages/litigation/casemgmt.html"
               cookies=p_cookie
               response = requests.get(url, headers=headers, cookies=cookies)
               print("Ln 594 Updated the Noties.... " + str(url))
               print(f"Status Code........................... CASE Management.html : {response.status_code}")
               received_cookie = response.cookies.get_dict()
               ##    print("Response Cookies : ", received_cookie)
               p_cookie = cookie_update(p_cookie, received_cookie)
               

               url = "https://services.gst.gov.in/services/api/ustatus"

               headers = {
               ##    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
               ##    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
               ##    "Cookie": f"TS01b8883c={cookies_TS01b8883c['TS01b8883c']};ak_bmsc={cookies_ak_bmsc['ak_bmsc']}",
                    "Host": "services.gst.gov.in",
                    "Pragma": "no-cache",
                    "Referer": "https://services.gst.gov.in",
                    "Sec-Fetch-Dest": "image",
                    "Sec-Fetch-Mode": "no-cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
               }

               cookies=p_cookie
               response = requests.get(url, headers=headers, cookies=cookies)

               print(f"Status Code.............................. Ustatus............: {response.status_code}")
               received_cookie = response.cookies.get_dict()
               ##    print("Response Cookies : ", received_cookie)
               p_cookie = cookie_update(p_cookie, received_cookie)
               print("Response for ustatus L/ine 690 : \n",response.text)   

               url="https://services.gst.gov.in/litserv/auth/api/case/folder"
                    #https://services.gst.gov.in/litserv/auth/api/case/folder

               headers = {    
               ##    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
               ##    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
               ##    "Cookie": f"TS01b8883c={cookies_TS01b8883c['TS01b8883c']};ak_bmsc={cookies_ak_bmsc['ak_bmsc']}",
                    "Host": "services.gst.gov.in",  
                    "Pragma": "no-cache",
                    "Referer": "https://services.gst.gov.in",
                    "Sec-Fetch-Dest": "image",
                    "Sec-Fetch-Mode": "no-cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\"",
               }
               #print("#################################### Temp addl notice payload",payload_temp_addlnotices)
               #payload =  
               '''
               payload = {
                              "caseId":3687612,
                              "gstid":"33AAYCS3291C2Z3",
                              "caseTypeCd":"ADJDT"
                              
                         }
               '''
               #payload = "{caseId:4111082,gstid:\"33AAYCS3291C2Z3\",caseTypeCd:\"ADJDT\"}"
               print("The Payload is  ............................................", payload)
               
               cookies=p_cookie
               print("#########################################3 Cookie is updated ................................")
               print(url, headers, cookies, payload)
               for index, row in df_reduced.iterrows():
                    #print(f"Processing caseTaskId: {row['caseTaskId']}, ARN: {row['arn']}, Case Type: {row['caseTpeCd']}, Case ID: {row['caseId']}")
                    payload = {
                              "caseId":row['caseId'],
                              "gstid":gstin,
                              "caseTypeCd":row['caseTpeCd']
                              
                         }
                    
                    print("The updated iterated payload is here ", payload)
               
                    response = requests.post(url, headers=headers, cookies=cookies, json=payload)

                    print("Ln 560 Updated the Detailed Addl additional Notices.... " )
                    print(f"Status Code is .......................: {response.status_code}")
                    received_cookie = response.cookies.get_dict()
                    print("Response Cookies : ", received_cookie)
                    p_cookie = cookie_update(p_cookie, received_cookie)
                    print("Updated Cookie : ", p_cookie)
                    print("Response for Addl notice Line 569 : \n",response.text)   
                    response_data = response.json()

                    current_directory1 = "C:/Users/RAMOFFICE3/OneDrive/Desktop/Manam_Final/Manam_Final/OutputFile/"
                    
                    file_path = current_directory1 + "\\" + folder_path +"\\"+ "Addl Notices- ext" + bname+ "_" + gstin + "_" + ".json"
                              
                              #ZipFile.write(file_path)
                    # re = response.to_dict()
                    # Save the response message as a JSON file
                    with open(file_path, 'w') as json_file:
                         json.dump(response_data, json_file)
                         # Convert JSON data to a DataFrame
                    df = pd.json_normalize(response_data)
                    
                    print("dataframe is here Line 604 ", df.head())
                    # Save DataFrame to Excel
                    output_file = current_directory1 + "\\" + folder_path + "\\Addl _notices_data ext.csv"
                    output_file_te = current_directory1 + "\\" + folder_path + "\\Det_Addl _notices_data ext - " + str(row['caseId']) + ".csv"
                    df['Gstin'] = gstin
                    df['Case ID'] = row['caseId']
                    df['caseTypeCd'] = row['caseTpeCd']
               # Display the updated DataFrame
                         
                    print(df)
                    df.to_csv(output_file_te, index=False)

                    #current_directory1 = "/home/bestmana/GSTDEMO/OutputFile/"        
                    folder_to_zip = current_directory1 + "\\" + folder_path
                    output_zip_file = current_directory1 + "\\" + folder_path + '.zip'
               zip_folder(folder_to_zip, output_zip_file)
               mail(gstin,bname,output_zip_file)

          #return p_cookie

          def create_unique_folder(gstin):
                    # Get the current date and time
               now = datetime.datetime.now()
                         
                         # Format the date and time to create a unique folder name
               timestamp = now.strftime("%Y%m%d_%H%M%S")
                         
                         # Generate a random 10-character alphanumeric string
               random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
                         
                         # Create the full folder name
               folder_name = f"{timestamp}-{gstin}-{random_str}"
                         
                         # Create the full path for the new folder
               folder_path = os.path.join(folder_name)
               current_directory1 = "C:/Users/RAMOFFICE3/OneDrive/Desktop/Manam_Final/Manam_Final/OutputFile/"        
                         # Create the new folder
               print("The Folder and file being created is " , (current_directory1 + "\\" + folder_path) )
               os.makedirs(current_directory1 + "\\"+ folder_path)
                         
               return folder_path

          def mail(gstin,bname,output_zip_file):
                     
               port = 465
               user = yagmail.SMTP(user='ramajayambot@gmail.com',password="waaouclyqtzgdzdb",port=port) 
               user.send(to ='accounts@ramajayam.in', subject ='GST Automation Email - ' + gstin +'-'+ bname ,contents ='This is test mail for python automation', attachments = output_zip_file) 
               print("EMAIL SENT !!!")


          

          def zip_folder(folder_path, output_path):
               with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    for root, _, files in os.walk(folder_path):
                         for file in files:
                              file_path = os.path.join(root, file)
                              arcname = os.path.relpath(file_path, start=folder_path)
                              zipf.write(file_path, arcname)


          def create_unique_folder2():
               print("############################# Started Def Create Unique Folder 2 Line 579")
                         # Get the current date and time
               now = datetime.datetime.now()            
                         # Format the date and time to create a unique folder name
               timestamp = now.strftime("%Y%m%d_%H%M%S")            
                         # Generate a random 10-character alphanumeric string
               random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
                         # Create the full folder name
               folder_name = f"{timestamp} Captcha {random_str}"
                         # Create the full path for the new folder
               folder_path = os.path.join(folder_name)
                         # Create the new folder
               os.makedirs(folder_path)            
               print("############################# End Def Create Unique Folder 2 Line 592")
               return folder_path

          def Captchaconvert(unique_folder):
               print("############################# Start Captchaconvert Line 595" )
               from twocaptcha import TwoCaptcha
               api_key = os.getenv('APIKEY_2CAPTCHA', '63b45c21d94e44ca13b67ff495562bc3')
               solver = TwoCaptcha(api_key)
               try:
                    result = solver.normal(unique_folder + "\\captcha.png")
               except Exception as e:
                    sys.exit(e)
               else:
                    print('solved: ' + str(result))      
               captchaCode = result['code']
               result['code']
               #captchaCode
               print("Hi " + captchaCode)
               print("############################# End Captcha Convert Line 611")
               return captchaCode
          
          def cookie_update(pm_cookie, received_cookie):
               print("############################# Started Cookie Update LLine 614")
               for key, value in received_cookie.items():
                    if key in pm_cookie:
                         pm_cookie[key] = received_cookie[key]
                    else:
                         pm_cookie[key] = value
               print("############################# End Cookie update  Line 620")        
               return pm_cookie 

          #userid = "svmpvtgst"
          #pwd = "Cbs@2029"

          ###Code Starts Here
          p_cookie , captchaCode = login(userid, pwd)

          #captchaCode = Captchaconvert()

          #folder_path = create_unique_folder(gstin)
          #captchaCode = input("Enter the Captcha: ") 
          #p_cookie = input("Enter the P Cookie: ") 
          #result['code']
          #captchaCode# = str(captchaCode)
          #print(captchaCode)
          #print(p_cookie)
          print("###################################### Moving to Login")
          complete_login(userid,pwd,captchaCode,p_cookie)

          #print(p_cookie)

    return render(request, 'index.html')
