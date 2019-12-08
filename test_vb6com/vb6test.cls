VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
  Persistable = 0  'NotPersistable
  DataBindingBehavior = 0  'vbNone
  DataSourceBehavior  = 0  'vbNone
  MTSTransactionMode  = 0  'NotAnMTSObject
END
Attribute VB_Name = "vb6test"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = True
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = True
Public m_form As Form

Public m_image As StdPicture

Public m_variant As Variant

Private m_int As Long

Public Function up_str(ByVal x As String, ByRef a As String) As Long
    a = UCase(a)
    up_str = Len(a) + Len(x)
End Function
