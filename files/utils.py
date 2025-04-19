import hashlib

class UserFileUtil:
    
    @staticmethod
    def compute_file_hash(file_obj, chunk_size = 8192):
        hasher = hashlib.sha256()
        for chunk in file_obj.chunks(chunk_size):
            hasher.update(chunk)
        return hasher.hexdigest()
    