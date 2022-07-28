# -*- coding: utf-8 -*-


import string

#This is the plain-text to be encrypted. Do Not delete this!
plain_text = list(input(""))

#This is the easy secret message for optional decryption
easy_secret = """S xgjx llvkek, cmwv wsk hvctxbui - jvvx ar Jfyllsp."""
message = len(plain_text)

key = list("SECRET"*message)

#This is the Full secret message for optional decryption
secret_message = """Gchl kdcey sor fynfb lyssg nag pie zsuvrlk cfboyih sijuv bh liwf 
wgohvhwoh, n hwx bnnapb, pifdsvpwe wa Facsenq, bbq xwewpulfr gi lis clgqcfcljca 
nzbh nfd nsa ujf qeysusq yivoy.

Hgx kr ujf saashsq cf b ueysu qvpam knl, lfggcfh kuylise nzbh auljca, ij bbl hsuwbh 
kp qbhufwiyv bbq mg esqcubhrx, ubb yifh saxmss. Jy sss zyl pb n ajfog vsuhyy-xjsyx 
gg huul xoe. Qw ioiy upar ng esqcubhr u hpfgcgo cs nzbh scwmr, nm s gwaud ssfnaou 
cfsds sij uvbmw xvb bwss tunf huyas zvpwt huul uvnn fbhvif nwtbl mwiy. Au wf uductylise 
zauhvhy bbq jjpdrl liog qw tvbode rb nzvg.

Ool, jb n fssurl kfbfy, of qnh fph qyvjqnnw -- xs puf ocg wgogrwjbhr -- qw doa hgu 
vnfdpk -- gbat ueimor. Gbw cfnpw nsa, fawwaa sor qyse, kui kufhaymsq bwss, uunf 
qbhkfqeulfr vn, xbf nvgws boj qcbl hpkrl lp oqx gs rrnjbqg. Nzf kblde kvfd mwgndf 
bbnw, oce fgou eyefaoyj xvnn of gns zffr, vmu wg wso brpws tblyfh jbsu huyq ewq 
bwss. Vn at tbl mt huy djjvhy, sogbws, hb vw esqcubhrx zffr ng uvr ofgwackisq qgsy 
jbadv gbwz kui xpitbl isey zbjr nzvg suj tc aitmm nxnbbpyv. Jh vm jbhuyj gce ok 
uc oy zffr xwewpulfr gi lis tlwbh gukl frgsjbvhy cssijf if -- nzbh slgn huykf vbhgssq 
xwbr jy lbyr cfdfrukfr qynphvif uc gbsu qnokf tbl oiwpb lisl asws gbw mofn xvzy 
gwbghlw pt qynphvif -- uvnn of vrlw iwtbdz frmgmjr nzbh gbwts qyse guudm bbn zbjr 
xafr vh nbwa -- nzbh gbat bnnapb, hhvff Tiv, tvnfd ioiy s osj vashu ix gfryvpa -- 
nhv uvnn ypjrlfnsan gg huy hfccfw, cm gbw qsbjdf, tbl lis cygqzr, mzbzy hgu drlatv 
slgn huy wbfgb."""

#TO DO:
#1. Ask the user for a code word and store it for use later

#2. Call an encryption function with the plainText above and the code word and save the result it gives back (cypher-text)

#3. Print out the cypher-text <-- This is the goal of the assignment!  

#4. Write the function to encrypt some text with a code word

#5. Write the helper functions needed to do the encryption (encrypt a letter)


def encrypt_letter(text_letter, code_letter):
    letters = list(string.ascii_uppercase) # Get the all the letters
    temp = text_letter.upper()
    letter_index = letters.index(temp)
    code_index = letters.index(code_letter)
    letters = letters[code_index:] + letters[:code_index]
    result = letters[letter_index]
    if text_letter.islower():
        result = result.lower()
    return result

#6. Optional: Write and call a decryption function on the secret message above

#Some tests of the functions. Be sure to delete these
x = len(list(plain_text))

y = plain_text 

for i in range(x):
  print(encrypt_letter(plain_text.pop(0), key.pop(0)),end="")


