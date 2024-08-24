import requests
from PIL import Image
from io import BytesIO
import json
from pprint import pprint
#from gstdata_to_df import gstr2b_to_excel
import pandas as pd
import ast
import shutil
import sys
import os
import datetime
import random
import string
import openpyxl
import csv
import os
import datetime
import random
import string
import os
import zipfile
#sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

#print(pwd)

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
        
        image.save(unique_folder + "\\captcha.png", format="PNG")
        print("Image saved successfully in the folder " + unique_folder )
        
        captchaCode = Captchaconvert(unique_folder)
        print("############################################ Call Captchaconvert(unique_folder) Line 181 ")
        image_path = os.path.join(unique_folder, "captcha.png")
        print("Image saved successfully as captcha.png")
        print("################################## Line 184")
        # Define the new file name
        
        new_image_path = os.path.join(unique_folder, captchaCode +".png")
        new_image_path2 = os.path.join("Image_dump", captchaCode +".png")
        print("Old Image path is :", new_image_path)
        print("################################## Line 189")
        print("New Image path is :", new_image_path2)
        print("########################################## Line 189")
        # Rename the files
        print("################################## Line 192")
        os.rename(image_path, new_image_path)

        shutil.move(new_image_path, new_image_path2)
        
        print("File Renamed successfully")
        print(captchaCode)
        
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
    current_directory1 = os.getcwd()   
    output_filebas = current_directory1 + "\\All_Basic_notices_data.csv"
    output_file2addl = current_directory1 + "\\All_Addl_notices_data.csv"
    output_file2add2 = current_directory1 + "\\All_Addl_notices_data_folder.csv"
    output_file3 = current_directory1 + "\\Login Status.csv"

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

    print(f"Status Code: {response.status_code}")
    record = [userid, pwd, {response.status_code, 'Login Status'}]
    with open(output_file3, mode='a', newline='') as file:
        writer = csv.writer(file)
    # Append the record
        writer.writerow(record)
    
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
    timestamp2 = now.strftime("%Y%m%d_%H%M%S") 
    record = [userid, pwd, "Done for Login Page", timestamp2, gstin, bname]
    
    with open(output_file3, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Append the record
        writer.writerow(record )
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
    timestamp3 = now.strftime("%Y%m%d_%H%M%S") 
    record = [userid, pwd, "Done for filingsnapshot", timestamp3, gstin, bname]
    
    with open(output_file3, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Append the record
        writer.writerow(record )
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

    current_directory1 = os.getcwd()        

    

    file_path = current_directory1 + "\\" + folder_path +"\\"+ "Notices-" + bname+ "_" + gstin + "_" + ".json"
            
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
    output_file = current_directory1 + "\\" + folder_path + "\\notices_data.csv"
    df.insert(20, "GSTIN", gstin + bname, True)
    df.to_csv(output_file, index=False)
    df.to_csv(output_filebas, mode='a', index=False)

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

    current_directory1 = os.getcwd() 

    file_path = current_directory1 + "\\" + folder_path +"\\"+ "Addl Notices-" + bname+ "_" + gstin + "_" + ".json"
            
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
    df.insert(0, "GSTIN", gstin + bname, True)
    df.to_csv(output_file, index=False)
    df.to_csv(output_file2addl, mode='a', index=False)
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

        current_directory1 = os.getcwd() 
        
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
        df.insert(0, "GSTIN", gstin + bname, True)
        df.to_csv(output_file_te, index=False)
        df.to_csv(output_file2add2, mode='a', index=False)

        

            
        current_directory1 = os.getcwd()        
        folder_to_zip = current_directory1 + "\\" + folder_path
        output_zip_file = current_directory1 + "\\" + folder_path + '.zip'
    record = [userid, pwd, "Done for Addl Folders"]
    
    with open(output_file3, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Append the record
        writer.writerow(record )

    #==============================================================================================================================
    #==============================================================================================================================
    #==============================================================================================================================
    #==================================LIABILITY===================================================================================
    #==============================================================================================================================
    #==============================================================================================================================
    #==============================================================================================================================
    #==============================================================================================================================
    #==============================================================================================================================
    #==============================================================================================================================

    
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://payment.gst.gov.in/payment/auth/ledger/paymenttowardsdemand",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "X-Kl-Saas-Ajax-Request": "Ajax_Request",
    }
    
    url = "https://payment.gst.gov.in/pages/common/menu.html"
    cookies=p_cookie
    response = requests.get(url, headers=headers, cookies=cookies)
    print("Ln 594 Updated the Noties.... " + str(url))
    print(f"Status Code........................... /common/menu.html : {response.status_code}")
    received_cookie = response.cookies.get_dict()
##    print("Response Cookies : ", received_cookie)
    p_cookie = cookie_update(p_cookie, received_cookie)
    
    url = "https://payment.gst.gov.in/pages/common/footer.html"
    cookies=p_cookie
    response = requests.get(url, headers=headers, cookies=cookies)
    print("Ln 594 Updated the Noties.... " + str(url))
    print(f"Status Code...........................s/common/footer.html : {response.status_code}")
    received_cookie = response.cookies.get_dict()
##    print("Response Cookies : ", received_cookie)
    p_cookie = cookie_update(p_cookie, received_cookie)
    
    url = "https://payment.gst.gov.in/pages/payment/outstandingdemand.html"
    cookies=p_cookie
    response = requests.get(url, headers=headers, cookies=cookies)
    print("Ln 594 Updated the Noties.... " + str(url))
    print(f"Status Code........................... CASE outstandingdemand.html : {response.status_code}")
    received_cookie = response.cookies.get_dict()
##    print("Response Cookies : ", received_cookie)
    p_cookie = cookie_update(p_cookie, received_cookie)
    
    url = "https://payment.gst.gov.in/services/api/ustatus"

    headers = {
    ##    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    ##    "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
    ##    "Cookie": f"TS01b8883c={cookies_TS01b8883c['TS01b8883c']};ak_bmsc={cookies_ak_bmsc['ak_bmsc']}",
        "Host": "payment.gst.gov.in",
        "Pragma": "no-cache",
        "Referer": "https://payment.gst.gov.in",
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


    url="https://payment.gst.gov.in/payment/auth/api/liabilitydetails?refLiabId="

    cookies=p_cookie
    headers = {    
        "Accept" : "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Host": "payment.gst.gov.in",  
        "Referer": "https://payment.gst.gov.in",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "X-KL-saas-Ajax-Request": "Ajax_Request",
        "sec-ch-ua-platform": "\"Windows\"",
    }
    #print("#################################### Temp addl notice payload",payload_temp_addlnotices)
    payload = {
                "refLiabId="
                
             }
    
    response = requests.get(url, headers=headers, cookies=cookies)
    print("Response for Liability ID line 815 : \n",response.text)   
    print("Response for Liability ID line 815 : \n",response.json)   
    print("Ln 809  Liability ID .... " )
    print(f"Status Code is ........Liability ID...............: {response.status_code}")
    received_cookie = response.cookies.get_dict()
    print("Response Cookies : ", received_cookie)
    p_cookie = cookie_update(p_cookie, received_cookie)
    print("Updated Cookie : ", p_cookie)
    print("Response for Liability ID line 815 : \n",response.text)   
    response_data = response.json()
 
    
    current_directory1 = os.getcwd() 
        
          

            # Convert JSON data to a DataFrame
    df = pd.json_normalize(response_data)
        
    print("dataframe is here Line 826 ", df.head())
        # Save DataFrame to Excel
    output_filelaib = current_directory1 +  "\\Liability.csv"
       # df = pd.json_normalize(response_data)
    
    print("The filtered Liability is ", df.head())

    df.insert(0, "GSTIN", gstin + bname, True)    
      
    print("The filtered Liability is ", df.head())    
    df.to_csv(output_filelaib, mode='a', index=False)
    timestamp1 = now.strftime("%Y%m%d_%H%M%S") 
    record = [userid, pwd, "Done for Liability", timestamp1]
    
    with open(output_file3, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Append the record
        writer.writerow(record )
     
        
    zip_folder(folder_to_zip, output_zip_file)
    #mail(gstin,bname,output_zip_file)
    
    
    
    
    
    
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
    current_directory1 = os.getcwd()        
            # Create the new folder
    print("The Folder and file being created is " , (current_directory1 + "\\"+ folder_path) )
    os.makedirs(current_directory1 + "\\"+ folder_path)
            
    return folder_path

def mail(gstin,bname,output_zip_file):
            import yagmail 
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






file_path = 'C:/Users/RAMOFFICE3/OneDrive/Desktop/Manam_Final/Manam_Final/Client Data.csv'

# Read specific columns
df = pd.read_csv(file_path, usecols=['User Name', 'Password'])

# Loop through the DataFrame and print values from each row
for index, row in df.iterrows():
    print(f"Column1: {row['User Name']}, Column2: {row['Password']}")

    
    userid = row['User Name']
    pwd = row['Password']
    print("The current data is   :", userid,  pwd)
    try:
        p_cookie , captchaCode = login(userid, pwd)

        print("###################################### Moving to Login")
        complete_login(userid,pwd,captchaCode,p_cookie)
        
    except:
        
        

#print(p_cookie)
        print("Done", userid)




'''
Total Process is here 



>> p_cookie, captchaCode = login(userid, pwd)                                      - Line 24  - Line 216
    >>>> Calls
        url = "https://static.gst.gov.in/uiassets/css/fonts/minified/FontAwesome.woff2?v=4.7.0"
        url = "https://services.gst.gov.in" 
        url = "https://services.gst.gov.in/services/api/ustatus" 
            >>>> Setting Up Business name and GSTIN            
        url = "https://services.gst.gov.in/services/captcha"   - Getting Captcha here  
    >>>unique_folder = create_unique_folder2()
    >>>> captchaCode = Captchaconvert(unique_folder)
    >>>>Return (p_cookie, captchaCode)


>> complete_login(userid,pwd,captchaCode,p_cookie)                    - Line 219 - Line 531
    >>> folder_path = create_unique_folder(gstin)
        >>>> Calls

        url = "https://services.gst.gov.in/services/authenticate"
        url = "https://services.gst.gov.in/pages/services/data/corbustype.json"
        url = "https://services.gst.gov.in/services/api/ustatus"
        url = "https://services.gst.gov.in/services2/auth/web/gta/decldtls/getNewTpGTADtls"
        url = "https://services.gst.gov.in/returns/auth/api/filingsnapshot"
        url ="https://return.gst.gov.in/returns/auth/api/rolestatus?rtn_prd=042023"
        url ="https://return.gst.gov.in/returns/auth/api/gstr3b/summary?rtn_prd=" + (x)
        url ="https://gstr2b.gst.gov.in/gstr2b/auth/api/gstr2b/getjson?rtnprd=" + (x)
 
        >>> Basic Notices
        
        >>>> Calls
        url = "https://services.gst.gov.in/services/api/ustatus"
        >>> Addl Notices
        >>> Folders - Addl Notices
    
    
    >>> zip_folder(folder_to_zip, output_zip_file) 
    >>> mail(gstin,bname,output_zip_file)

    
def create_unique_folder(gstin):                                       - Line 538 - 555
def mail(gstin,bname,output_zip_file):                              - Line  558 - 563
def zip_folder(folder_path, output_path):                           - Line 569 - 576
def create_unique_folder2():                                            -Line 579 - 592
def Captchaconvert(unique_folder):                                      - Line 595 - 611
def cookie_update(pm_cookie, received_cookie):                      -- Line 614 - 620



Generate GSTR 1 Document
https://return.gst.gov.in/returns/auth/api/offline/download/generate?flag=1&rtn_prd=032024&rtn_typ=GSTR1
flag=1&rtn_prd=032024&rtn_typ=GSTR1
https://return.gst.gov.in/returns/auth/api/offline/download/generate?flag=0&rtn_prd=032024&rtn_typ=GSTR1
flag=0&rtn_prd=032024&rtn_typ=GSTR1

{
    "status": 1,
    "data": {
        "status": 0,
        "msg": "You have downloaded the file last on 17/06/2024 at 17:35:40. To view the same file, click on the link available below the button. To generate the latest file, click on the download button again",
        "url": [
            "https://files.gst.gov.in/returns/17062024/R1/f49f2cd88d2c4be79a20062934bcb02d/returns_17062024_R1_33AAUFV5960A1ZZ_offline_others_0.zip?md5\u003dkifyAlMT4cXr2nE4St1cVg\u0026expires\u003d1718626107"
        ],
        "date": "17/06/2024",
        "time": "17:35:40",
        "timeStamp": "2024-06-17 17:35:40.0",
        "rc": 1
    }
}





'

\\\] ,
https://return.gst.gov.in/returns/auth/api/offline/download/generate?flag=0&rtn_prd=032024&rtn_typ=GSTR2A


flag=0&rtn_prd=032024&rtn_typ=GSTR2A



CASE STATUS


Folder 
POST
	https://services.gst.gov.in/litserv/auth/api/case/folder
 {"caseId":6778667,"gstid":"33AACCC8751D1ZX","caseTypeCd":"ADJDT"}
 

[{"caseFolderId":39866476,"caseFolderTypeCd":"INTIM","caseFolderTypeName":"INTIMATIONS","caseTypeCd":null,"stateJursdCd":null,"userId":null,"ipAddress":null,"accessType":"W","casefolderseq":1},{"caseFolderId":39866477,"caseFolderTypeCd":"NOTCE","caseFolderTypeName":"NOTICES","caseTypeCd":null,"stateJursdCd":null,"userId":null,"ipAddress":null,"accessType":"R","casefolderseq":2},{"caseFolderId":39866481,"caseFolderTypeCd":"REPLY","caseFolderTypeName":"REPLIES","caseTypeCd":null,"stateJursdCd":null,"userId":null,"ipAddress":null,"accessType":"W","casefolderseq":3},{"caseFolderId":39866478,"caseFolderTypeCd":"ORDRS","caseFolderTypeName":"ORDERS","caseTypeCd":null,"stateJursdCd":null,"userId":null,"ipAddress":null,"accessType":"R","casefolderseq":5}]


POST
	https://services.gst.gov.in/litserv/auth/api/case/folder/items
 {"caseFolderId":39866476}
 
 

0	Object { itemJson: '{"arn":"AD331223057390I","arndt":"27/12/2023","gstin":"33AACCC8751D1ZX","state_cd":"33","refid":"ZD331223215715R","todtls":{"toid":"B33000000038762","dg":"Deputy Commercial Tax Officer","nm":"KANNAN ","pl":"TN339","jurscd":"TN339","pn":"AIZPK3681N"},"refdt":"27/12/2023","act_cd":"ADJDT_NOTCE_DTSCN","sdtls":{"dtscn":{"dmddtls":[{"tp":{"fromm":"04","fromy":"2018","tom":"03","toy":"2019"},"dact":"IGST","dfees":"","dtot":"2894604.00","pos":"Andhra Pradesh","dtax":"1416073","trnovr":"","dist":"1335221","dpnlty"…:"IGST, CGST and SGST ACT 2017","suppdocs":[{"dcupdtls":{"docName":"SPACEAGE STORAGE CONCEPTS PRIVATE LIMITED.pdf","id":"20231233502365","ct":"application/pdf","ty":"ADJN","hash":"e8e7cb8d6f573d6d6ab82e9355316a636c5fda6422fd102ab54f32d7bf4f2827","name":"DRC 01"}}],"maindocs":[{"dcupdtls":{"id":"20231233502391","docName":"DOT_NOTICE_ZD331223215715R_20231227120635.pdf","ct":"application/pdf","ty":"ADJN","hash":"967a54a50ae33362dfe0711f0cd40c0b14fbf6234b51f6ee85b5ca6184c6a541"}}],"fetr":"N","pershrng":"N"}}}', itemId: 40256587, caseFolderId: 39866477, … }
1	Object { itemJson: '{"arn":"AD331223057390I","arndt":"27/12/2023","gstin":"33AACCC8751D1ZX","state_cd":"33","refid":"ZD330224016283Y","todtls":{"toid":"B33000000038762","dg":"Deputy Commercial Tax Officer","nm":"KANNAN ","pl":"TN339","jurscd":"TN339","pn":"AIZPK3681N"},"refdt":"03/02/2024","act_cd":"ADJDT_NOTCE_REMND","ntref":"ZD331223215715R","ntcdt":"27/12/2023","sdtls":{"remnd":{"fy":"2018-2019","type":"REMINDER","sec":"73","duedt":"19/02/2024","remno":"1","suppdocs":[{"dcupdtls":{"docName":"Personal Hearing.pdf","id":"2024023342950","ct":"application/pdf","ty":"ADJN","hash":"0ef0c75abb2ecd5eb30e4e520cd8fca42259128b5201b06709e66715bfbaad58"}}],"maindocs":[{"dcupdtls":{"id":"2024023342968","docName":"DOT_REMINDER_ZD330224016283Y_20240203050721.pdf","ct":"application/pdf","ty":"ADJN","hash":"3a2d1f2ebbf40397b6d5ca16575075919d5956c50dff85202fa4db0cbbadbd7c"}}],"pershrng":"N"}}}', itemId: 41097045, caseFolderId: 39866477, … }
2	Object { itemJson: '{"arn":"AD331223057390I","arndt":"27/12/2023","gstin":"33AACCC8751D1ZX","state_cd":"33","refid":"ZD3303242115403","todtls":{"toid":"B33000000038762","dg":"Deputy Commercial Tax Officer","nm":"KANNAN ","pl":"TN339","jurscd":"TN339","pn":"AIZPK3681N"},"refdt":"30/03/2024","act_cd":"ADJDT_NOTCE_REMND","ntref":"ZD331223215715R","ntcdt":"27/12/2023","sdtls":{"remnd":{"fy":"2018-2019","type":"REMINDER","sec":"73","duedt":"05/04/2024","remno":"2","suppdocs":[{"dcupdtls":{"docName":"Personal Hearing -2.pdf","id":"20240333497351","ct":"application/pdf","ty":"ADJN","hash":"9c4c13821d46dff17ecaf7c1fe302b2d9aae6be6859c3a9e68a998865bcf9591"}}],"maindocs":[{"dcupdtls":{"id":"20240333497355","docName":"DOT_REMINDER_ZD3303242115403_20240330051359.pdf","ct":"application/pdf","ty":"ADJN","hash":"eb133e7faf48fbbe5eaa8d2f30c3f92c81dd039c522a548f08e13e6498dc30cf"}}],"pershrng":"N"}}}', itemId: 42228626, caseFolderId: 39866477, … }




Liability List

https://payment.gst.gov.in/payment/auth/api/liabilitydetails?refLiabId=

refLiabId=


https://payment.gst.gov.in/payment/auth/api/liabilitydetails?refLiabId=
Request Method:
GET

Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: en-US,en;q=0.9
Connection: keep-alive
Cookie: AuthToken=f7ef7797450642a598f5c9eca005dd61; UserName=ventureaccounts; EntityRefId=T330000001881; TS0123b7b3=0140752c73775d8c9d1d91d1441f0ba9c57aad751901a1f2f1f126197870cd773179095086f491ca4b5942a509d0ad79c1a8a98c91; Lang=en; ak_bmsc=2D49D4A90632922D40424FBDA631ECDB~000000000000000000000000000000~YAAQdAosF5PQ7HiQAQAADF5ieRhZ5BouZhQN3LVHWalw1OW1eNeMrJcA8XX9VpEM/pQkvT/hnd/inu8DgZKQQyTflyyNilyEtSWEtZ0o2PGMCdUmqzRN/P14r8XLn2LDcw0NnkFiLDJ00847RPQFHmnPNZ2HysF+8+wRaRnqZEWMY7wlMYyYtHO1ql0hCSp/qJwoR5QxgiOkgJau1zXwf4WPSltD/iGrGYlBdpp9hodOgs48qqNuv3FbUfNQ/ZHlxe3/otyNixXisK25z6CcCB+iYe+xd+Uf96BUvVo2SdRB/Vz2auXXXPKB45Um3zrMSd+CTf40EFUUVJmiIGpampPwYCPqGaT7ELtmMEXGL0fyI9pcmq58t9kvSj5EbaI=; bm_sv=C33B55CEE7DB26A555C2095E28385176~YAAQdAosF6vQ7HiQAQAAQHxieRgxVIjT/6skyBJP6JKP12vHaCvunHzHi4tde0WAiXle/p1gwwtkX083RFFuMBymWilTYQFiQrauYWhFZL7rKdsmvr48lG8BObsQvTNmmfmOiMegqEeAgXWl1hJox8iO9Mk3qpWZ7ABCTnuH8IkJ/uTkuoygdRGzSCld5kxMbYrUCqggOST91EDiWjFucHUNGUvtAVsiDFCZoIpheGbIm6RgA5TfyNRyhgbm9l9A~1
Host: payment.gst.gov.in
Referer: https://payment.gst.gov.in/payment/auth/ledger/paymenttowardsdemand
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
X-KL-saas-Ajax-Request: Ajax_Request
sec-ch-ua: "Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"




















'''

print()