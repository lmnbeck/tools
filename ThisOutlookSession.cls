VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "ThisOutlookSession"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Private Sub Application_ItemSend(ByVal Item As Object, Cancel As Boolean)
    Dim objRecip As Recipient
    Dim objContact As ContactItem
    Dim strInternal As String
    Dim strExternal As String

    If Item.MessageClass Like "IPM.TaskRequest*" Then
        Set Item = Item.GetAssociatedTask(False)
    End If
    strInternal = "内部发送:" & vbCr
    strExternal = "外部发送:" & vbCr
    
    For Each objRecip In Item.Recipients
        Set objContact = FindContactByAddress(objRecip.Address)
        
        If LCase(objRecip.Address) Like "/o=*" Then
            strInternal = strInternal & objRecip.Name & vbCr
        Else
            strExternal = strExternal & objRecip.Name & vbCr
        End If
        
'        If objContact Is Nothing Then
'            If LCase(objRecip.Address) Like "/o=*" Then
'                strExternal = strExternal & "内部发送" & objRecip.Name & vbCr
'            Else
'                strExternal = strExternal & "外部发送" & objRecip.Name & vbCr
'            End If
'        End If
    Next
    
    If strInternal <> "" And strExternal <> "" Then
                  MSGText = "主题：「" & Item.Subject & "」" & vbCr & "要向下面的地址发送邮件，确定吗？" & _
        vbLf & "收信人地址:" & vbCr & strInternal & strExternal
        If MsgBox(MSGText, vbYesNo, "发送确认") = vbNo Then
            Cancel = True
        End If
    End If
End Sub



Private Function FindContactByAddress(strAddress As String)
Dim objContacts
    Dim objContact
    Set objContacts = Application.Session.GetDefaultFolder(olFolderContacts)
    Set objContact = objContacts.Items.Find("[Email1Address] = '" & strAddress _
        & "' or [Email2Address] = '" & strAddress _
        & "' or [Email3Address] = '" & strAddress & "'")
    Set FindContactByAddress = objContact

End Function
