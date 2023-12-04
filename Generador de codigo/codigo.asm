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
EXIT2:
MOV AX,a_global
MOV BX,3
CMP AX,BX
JA ETIQ_CUMP1
JMP ETIQ_NOCUMP1
ETIQ_CUMP1:
MOV AX,a_global
MOV BX,1
SUB AX,BX
MOV a_global , AX
JMP EXIT2
ETIQ_NOCUMP1:
MOV AX,4C00H
INT 21H
BEGIN ENDP
END BEGIN