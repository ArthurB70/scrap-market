from cryptography.fernet import Fernet


KEY = b'mK0R64e82IFMVMM-PFDAW6MhKe7TWcNtTZ6_5IDQdyU='


fernet = Fernet(KEY)
    
def Encrypt(mensagem):
        return fernet.encrypt(bytes(mensagem.encode('utf-8'))).decode("utf-8")
    
def Decrypt(mensagem):
        return fernet.decrypt(mensagem).decode("utf-8")