PAGE 60,132
TITLE PROG1.EXE
.MODEL SMALL
.STACK 64
;-----------------------------------
.DATA
a_global DW ?
b_global DW ?
c_global DW ?
d_global DW ?
e_global DW ?
hola_main DW ?
mundo_main DW ?
;-----------------------------------
.CODE
BEGIN PROC FAR
MOV AX,@DATA
MOV DS,AX
MOV CX,5
MOV a_global , CX
MOV CX,2
MOV b_global , CX
MOV AX,b_global
MOV BX,b_global
MUL BX
MOV BX,a_global
ADD AX,BX
MOV c_global , AX
MOV AX,a_global
MOV BX,1
CMP AX,BX
JE ETIQ_CUMP1
JMP ETIQ_NOCUMP1
ETIQ_NOCUMP1:
MOV AX,b_global
MOV BX,2
CMP AX,BX
JE ETIQ_CUMP2
JMP ETIQ_NOCUMP2
ETIQ_CUMP1:
ETIQ_CUMP2:
MOV CX,3
MOV b_global , CX
JMP EXIT1
ETIQ_NOCUMP2:
MOV CX,5
MOV b_global , CX
EXIT1:
MOV AX,4C00H
INT 21H
BEGIN ENDP
END BEGIN