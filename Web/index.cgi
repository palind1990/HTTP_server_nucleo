t <head>
t <title>Web Server Demo</title>
t <script language=JavaScript type="text/javascript" src="xml_http.js"></script>
t <script language=JavaScript type="text/javascript">
t var formUpdate = new periodicObj("buttons.cgx", 300);
t function periodicUpdate() {
t  if(document.getElementById("refreshChkBox").checked == true) {
t   updateMultiple(formUpdate);
t   periodicFormTime = setTimeout("periodicUpdate()", formUpdate.period); 
t  }
t  else
t   clearTimeout(periodicFormTime);
t }
t </script></head>
t <body>
t <img src="vives_logo.png" >
t <h1>Justin Ooghe</h1>
t Counter: 
c f 3 <input type=text name=lcd3 size=20 maxlength=20 value="%d">
# t b 0 <input type=button name=led0 value=reset OnClick="submit();" %s>
t <form action="buttons.cgi" method="post" id="form1" name="form1">
t  BlueButton state: <input type="checkbox" disabled id="button0"><br />
t  Update state Periodic:<input type="checkbox" id="refreshChkBox" onclick="periodicUpdate()">
t </body>
t </html>
.




