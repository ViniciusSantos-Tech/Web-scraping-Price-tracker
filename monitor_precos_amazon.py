#𝙁𝙚𝙞𝙩𝙤 𝙥𝙤𝙧 𝙑𝙞𝙣𝙞𝙘𝙞𝙪𝙨 𝙎𝙖𝙣𝙩𝙤𝙨-𝙏𝙚𝙘𝙝
#𝗦𝗖𝗥𝗔𝗣𝗣𝗜𝗡𝗚 𝗔𝗠𝗔𝗭𝗢𝗡


from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
import time
import datetime

def Iphone():
    while True:
        print("|----RELATORIO-DO-DIA----")
        try:
            driver.get("https://www.amazon.com.br/Apple-iPhone-15-128-GB/dp/B0CP6CR795/ref=sr_1_1_sspa?crid=3G7RRG53BW6GI&dib=eyJ2IjoiMSJ9.2SIQoh28Cum9U_fAbRl-XnazhkdmCIxRh34UrGA5uPIODZ25L_b7pm32Q94iwhuCo2p8_pbsA6FFSF0JBxwKT0Di4Xe3-tTFiPgNt1z_V9MTlejuyr7hCdqLqBdXaGASgmLOGAf4x4vHCVtXrTQfZ8yVKMRGGFeTfuTh3WB9F7MK4-s2TFvaTKf37jeYzP1_9jUk5IijH4i64cAIb3-RRUuw8BC_fy9b9BGXOXXL-Y5D3dohQF23h_tUpq4o9vq7vj6_ET8BAs2R8EmwzGrCNcq3C16oyVxYXwjXIBgvHo4.SsvRJA9VWEPWEC-a6G7c0frf5vuYsYtkPFrbnQpbyTg&dib_tag=se&keywords=iphone%2B15&qid=1761916471&sprefix=i%C2%B4hone%2Caps%2C273&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.9e6a115c-05b9-4b96-8e1c-b1f9ce2ac1a6&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
            time.sleep(2)
            Local = driver.find_element(By.CSS_SELECTOR, '.a-size-large.product-title-word-break')
            Nome_Iphone = Local.text
            print(f"|Produto: {Nome_Iphone}")
            Preço_Iphone = driver.find_element(By.CSS_SELECTOR, ".a-price-whole").text
            print(f"|💸 Preço: R${Preço_Iphone}")
            Avaliaçao_Iphone1 = driver.find_element(By.CSS_SELECTOR, ".a-size-base.a-nowrap").text
            Avaliaçao_Iphone_Limpa = Avaliaçao_Iphone1[:3]
            print(f"|🏷️  Avaliaçao: {Avaliaçao_Iphone_Limpa}")
            DATA = datetime.date.today()
            print(f"|📆  Data: {DATA}")

            print("|-------------------------------------")
            Samsung()
            break
        except:
            print("|❌ Erro! Tentando novamente, aguarde.")
#--------------------------------------------------------
#--------------------------------------------------------
def Samsung():
    while True:
        try:
            driver.get("https://www.amazon.com.br/Smartphone-Motorola-Moto-g75-Ultrarresistencia/dp/B0DK7YSXLM/ref=sr_1_1_sspa?crid=2J1NVPI92SDAJ&dib=eyJ2IjoiMSJ9.30iIGkApvBP7gyzrKzolJIGnrgfyxeHBY5SW84xeqjhEmCmfdBWz-Fk3ysG9y2348eJUqakUnDIEx2ZnPNuTVZDvT709693iCVbtVvP-JdZC1U631sMKhIo5AZLqPujaOuSJeGnQBBA_hCWGrb15P11xS92thagwb1OG95ifUF6gxhvc6TP_MHJih_0k2BNORnnmwawzHAoiOZQuoSiifHmwNJPrK4IaOsJOIIVbUaX8L1-iG_JZrDXPkFk2zyGFTJJ-lHQ0KpxslsOgGCZz1IVhfIShHBxSCEeJcneXK5I.Rcux9Sji6_PvQ1guhW8vLTVT6KcqfBrf0ioVSUZAXYc&dib_tag=se&keywords=samsung%2Bs24&qid=1761920245&sprefix=SAM%2Caps%2C326&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.9e6a115c-05b9-4b96-8e1c-b1f9ce2ac1a6&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
            time.sleep(2)
            Local2 = driver.find_element(By.CSS_SELECTOR, '.a-size-large.product-title-word-break')
            Nome_Samgung = Local2.text
            print(f"|Produto: {Nome_Samgung}")
            Preço_Samsung = driver.find_element(By.CSS_SELECTOR, ".a-price-whole").text
            print(f"|💸 Preço: R${Preço_Samsung}")
            Avaliaçao_Samsung1 = driver.find_element(By.CSS_SELECTOR, ".a-size-base.a-nowrap").text
            Avaliaçao_Samsung_Limpa = Avaliaçao_Samsung1[:3]
            print(f"|🏷️  Avaliaçao: {Avaliaçao_Samsung_Limpa}")
            DATA = datetime.date.today()
            print(f"|📆  Data: {DATA}")
            print("|-----------------------------------------")
            xbox()
            break
        except:
            print("|❌ Erro! Tentando novamente, aguarde.")
def xbox():
       while True:
           try:        
                driver.get("https://www.amazon.com.br/Xbox-Controle-Din%C3%A2mica-Arquitetura-Velocity/dp/B0D932YWSZ/ref=sr_1_5?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1GAQW2CN5FOW6&dib=eyJ2IjoiMSJ9.OaLqtAdjk1FOHUvPtevvVTTaTniSgdHd67QeSmUiKmHyNDQFN_8XZvSSlCH7a3plw5CTqt_p80GEqLv4WBR_YKkXNMNISy3xLyGLj8NN-cku094zWm3hFjc_FuebpH2o--0dXY8i135b4D4buNO0gUVCVVTWE3kt7xWfVbU5sqLW5DCvSXV9RU1HaUPVfi5UbfmrP8XI-hRLRvVenpPboOsbRomweKeEt3LXUTiljok6N7XrL7cFdieAdo7znG0lIq86XZAvhqMs3Rb8us1JeKKVVo0AgHlWb498KLVYLDs.RowApXjM51pCzGQjyVGkFUT9zQs2lFAXgA7BpH_1Ij0&dib_tag=se&keywords=xbox%2Bseries%2Bs&qid=1761921127&sprefix=xbox%2Bseries%2Bs%2Caps%2C220&sr=8-5&ufe=app_do%3Aamzn1.fos.95de73c3-5dda-43a7-bd1f-63af03b14751&th=1")
                time.sleep(2)
                Local3 = driver.find_element(By.CSS_SELECTOR, '.a-size-large.product-title-word-break')
                Nome_Xbox = Local3.text
                print(f"|Podruto: {Nome_Xbox}")
                Preço_Xbox = driver.find_element(By.CSS_SELECTOR, ".a-price-whole").text
                print(f"|💸 Preço: R${Preço_Xbox}")
                Avaliaçao_Xbox1 = driver.find_element(By.CSS_SELECTOR, ".a-size-base.a-nowrap").text
                Avaliaçao_Xbox_Limpa = Avaliaçao_Xbox1[:3]
                print(f"|🏷️  Avaliaçao: {Avaliaçao_Xbox_Limpa}")
                DATA = datetime.date.today()
                print(f"|📆  Data: {DATA}")
                print("|-----------------------------------------")
                Playstation()
                break
           except:
                print("|❌ Erro! Tentando novamente, aguarde.")

def Playstation():
       while True:
           try:        
                driver.get("https://www.amazon.com.br/Console-PlayStation%C2%AE5-Edi%C3%A7%C3%A3o-Digital-825GB/dp/B0FPGF9J2J/ref=sr_1_5?crid=2V44249LCQ2V&dib=eyJ2IjoiMSJ9.Gc-m8nIZLRnG0y0IV8Vr2K1juNmsVETuIEQXbhh1rU-TEfiFUndY4MVeJgqoHRaymhrH7Co0RyJl2skn9jtanr5xMQ-0LN1HWUaf_NlbYAQMnrsYffsz37ZYqMLc3sVuq3pHeKw2CzVutavr0rkDTGNK6dT9jy0fl6at9HcgNs_Cloj2pokARTAKgscJwcEfbSU0TZ8guaTLBoeOkeK-wNS3OWf2e993dyadyDeFXXksZuhY6yXJyWDx_4uuG6hgD_BwTkCnspkKdvi3JCd5iQDJH8OqisBE1X_nnd_7UCc.mZmPmP0NknNqP2h4bjzsEG0WDPJE68yK_-BFbJjZ5Vw&dib_tag=se&keywords=playstation+5&qid=1761922666&sprefix=Pla%2Caps%2C243&sr=8-5&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147")
                time.sleep(2)
                Local4 = driver.find_element(By.CSS_SELECTOR, '.a-size-large.product-title-word-break')
                Nome_Ps = Local4.text
                print(f"|Podruto: {Nome_Ps}")
                Preço_Ps = driver.find_element(By.CSS_SELECTOR, ".a-price-whole").text
                print(f"|💸 Preço: R${Preço_Ps}")
                Avaliaçao_Ps1 = driver.find_element(By.CSS_SELECTOR, ".a-size-base.a-nowrap").text
                Avaliaçao_Ps_Limpa = Avaliaçao_Ps1[:2]
                print(f"|🏷️  Avaliaçao: {Avaliaçao_Ps_Limpa}")
                DATA = datetime.date.today()
                print(f"|📆  Data: {DATA}")
                print("|⏱️ Proxima atualizaçao daqui a 24Hrs.")
                print("|================================================================")
                driver.quit()
                time.sleep(86400)
                Iphone()
                break
           except:
                print("|❌ Erro! Tentando novamente, aguarde.")
Iphone()
