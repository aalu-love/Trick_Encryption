# Trick_Encryption
How to use:
<img src="images/use.png" alt="no_image"><br>
Step 1 : Clone or download the repo.
Step 2 : Extract the zip to your desktop.

Genrate Key:
>> py.exe T.py -k T -n 'KeyName.anything'
>> 5 (Remember the Code here)
<img src="images/keygen.png" alt="no_image"><br><br>

Message: <img src="images/msg.png" alt="no_image"><br>
Encryption:
>> py.exe T.py -en 'FileName' -key 'keyName.anything'
>> b'2X7dMLTgWcyNZq09-Bv-WxtOKiPR9QH0XWUmJvflpi8=\x02z'
>> 5
<img src="images/enmsg.png" alt="no_image"><br><br>

Decryption:
>> py.exe T.py -de 'FileName' -key 'keyName.anything' -t 5
<img src="images/demsg.png" alt="no_image"><br>
<img src="images/decode.png" alt="no_image"><br>

Know the key code:
>> py.exe T.py -load 'keyName.anything'
>> 122
Note : 5 + 5 = <b>10</b> (Key Code)
<img src="images/keycode.png" alt="no_image"><br>


<b> All done Enjoy the App.</b>
