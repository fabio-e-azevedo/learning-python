import re
import unicodedata

class StrTransformation:
    def __init__(self, string):
        self._string = string

    @property
    def lowercase(self):
        return StrTransformation(self._string.lower())

    @property
    def uppercase(self):
        return StrTransformation(self._string.upper())
    
    @property
    def spaces_by_underscore(self):
        return StrTransformation(self._string.replace(' ', '_'))

    @property
    def hiffen_by_underscore(self):
        return StrTransformation(self._string.replace('-', '_'))

    @property
    def trim(self):
        """Remove espaços em branco do início e fim."""
        return StrTransformation(self._string.strip())
    
    @property
    def single_underscores(self):
        """Método para remover underscores duplos ou mais."""
        return StrTransformation(re.sub('_+', '_', self._string))
    
    @property
    def without_accents(self):
        """Remove todos os acentos da string."""
        nfkd_form = unicodedata.normalize('NFD', self._string)
        without_accents_str = ''.join([c for c in nfkd_form if not unicodedata.combining(c)])
        return StrTransformation(without_accents_str)
    
    @property
    def without_special_characters(self):
        """Remove todos os caracteres especiais da string, mantendo apenas letras, números e hifens."""
        cleaned_str = re.sub(r'[^a-zA-Z0-9_]', '', self._string)
        return StrTransformation(cleaned_str)
    
    @property
    def transformers(self):
        return (
            StrTransformation(self._string)
            .trim
            .hiffen_by_underscore
            .spaces_by_underscore
            .single_underscores
            .without_accents
            .without_special_characters
        )
    
    @property
    def data(self):
        return self._string
    
    def __repr__(self) -> str:
        return self._string

a = StrTransformation('Teste! @#$%de*& ^string EspEcIaL.')
b = a.transformers

print(b.uppercase)
print(b.lowercase)