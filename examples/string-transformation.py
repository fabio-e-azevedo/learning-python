import re
import unicodedata

class StrTransformation:
    def __init__(self, string):
        self._string = string

    @property
    def lowercase(self):
        """
        Retorna uma nova instância com todos os caracteres em minúsculas.

        Returns:
            StrTransformation: nova instância contendo a string em minúsculas.
        """
        return StrTransformation(self._string.lower())

    @property
    def uppercase(self):
        """
        Retorna uma nova instância com todos os caracteres em maiúsculas.

        Returns:
            StrTransformation: nova instância contendo a string em maiúsculas.
        """
        return StrTransformation(self._string.upper())
    
    @property
    def spaces_by_underscore(self):
        """
        Substitui espaços por underscores (_) na string.

        Returns:
            StrTransformation: nova instância com espaços substituídos por '_'.
        """
        return StrTransformation(self._string.replace(' ', '_'))
    
    @property
    def spaces_by_hiffen(self):
        """
        Substitui espaços por hífens (-) na string.

        Returns:
            StrTransformation: nova instância com espaços substituídos por '-'.
        """
        return StrTransformation(self._string.replace(' ', '-'))

    @property
    def hiffen_by_underscore(self):
        """
        Substitui hífens (-) por underscores (_) na string.

        Returns:
            StrTransformation: nova instância com '-' substituído por '_'.
        """
        return StrTransformation(self._string.replace('-', '_'))

    @property
    def trim(self):
        """
        Remove espaços em branco no início e fim da string.

        Returns:
            StrTransformation: nova instância com espaços de borda removidos.
        """
        return StrTransformation(self._string.strip())
    
    @property
    def single_underscores(self):
        """
        Normaliza múltiplos underscores consecutivos para um único '_'.

        Returns:
            StrTransformation: nova instância com underscores simplificados.
        """
        return StrTransformation(re.sub('_+', '_', self._string))
    
    @property
    def single_hiffen(self):
        """
        Normaliza múltiplos hífens consecutivos para um único '-'.

        Returns:
            StrTransformation: nova instância com hífens simplificados.
        """
        return StrTransformation(re.sub('-+', '-', self._string))
    
    @property
    def without_accents(self):
        """
        Remove acentos/diacríticos da string usando normalização Unicode (NFD).

        Returns:
            StrTransformation: nova instância sem caracteres diacríticos.
        """
        nfkd_form = unicodedata.normalize('NFD', self._string)
        without_accents_str = ''.join([c for c in nfkd_form if not unicodedata.combining(c)])
        return StrTransformation(without_accents_str)
    
    @property
    def without_special_characters(self):
        """
        Remove caracteres especiais, mantendo apenas letras, dígitos e espaços.

        Returns:
            StrTransformation: nova instância com caracteres especiais removidos.
        """
        cleaned_str = re.sub(r'[^a-zA-Z0-9 ]', '', self._string)
        return StrTransformation(cleaned_str)
    
    @property
    def transformers(self):
        """
        Aplica uma sequência predefinida de transformações encadeadas.

        A sequência atual:
        - remove acentos
        - remove caracteres especiais
        - trim (remove espaços nas bordas)
        - substitui espaços por hífens
        - normaliza múltiplos hífens

        Returns:
            StrTransformation: nova instância resultante das transformações encadeadas.
        """
        return (
            StrTransformation(self._string)
            .without_accents
            .without_special_characters
            .trim
            # .spaces_by_underscore
            # .single_underscores
            .spaces_by_hiffen
            .single_hiffen
        )
    
    @property
    def data(self):
        """
        Retorna a string atual contida na instância.

        Returns:
            str: a string resultante das transformações aplicadas.
        """
        return self._string
    
    def __repr__(self) -> str:
        return self._string


a = StrTransformation(' ===>>> Tëste! @#$%de*&      ^striñg EspEcIaL.   ')
b = StrTransformation(' ===>>> Tëste! @#$%de*&      ^striñg EspEcIaL.   ').transformers.data

print(a)
print(b.lower())
