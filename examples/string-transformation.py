import re
import unicodedata


class StringTransformer:
    def __init__(self, string):
        self._string = string

    @property
    def lowercase(self):
        """
        Retorna uma nova instância com todos os caracteres em minúsculas.

        Returns:
            StringTransformer: nova instância contendo a string em minúsculas.
        """
        return StringTransformer(self._string.lower())

    @property
    def uppercase(self):
        """
        Retorna uma nova instância com todos os caracteres em maiúsculas.

        Returns:
            StringTransformer: nova instância contendo a string em maiúsculas.
        """
        return StringTransformer(self._string.upper())

    @property
    def space_to_underscore(self):
        """
        Substitui espaço por underscore (_) na string.

        Returns:
            StringTransformer: nova instância com espaço substituído por '_'.
        """
        return StringTransformer(self._string.replace(" ", "_"))

    @property
    def space_to_hyphen(self):
        """
        Substitui espaço por hífen (-) na string.

        Returns:
            StringTransformer: nova instância com espaço substituído por '-'.
        """
        return StringTransformer(self._string.replace(" ", "-"))

    @property
    def hyphen_to_underscore(self):
        """
        Substitui hífen (-) por underscore (_) na string.

        Returns:
            StringTransformer: nova instância com '-' substituído por '_'.
        """
        return StringTransformer(self._string.replace("-", "_"))

    @property
    def underscore_to_hyphen(self):
        """
        Substitui underscore (_) por hífen (-) na string.

        Returns:
            StringTransformer: nova instância com '_' substituído por '-'.
        """
        return StringTransformer(self._string.replace("_", "-"))

    @property
    def trim(self):
        """
        Remove espaços em branco no início e fim da string.

        Returns:
            StringTransformer: nova instância com espaços de borda removidos.
        """
        return StringTransformer(self._string.strip())

    @property
    def single_underscore(self):
        """
        Normaliza múltiplos underscores consecutivos para um único '_'.

        Returns:
            StringTransformer: nova instância com underscores simplificados.
        """
        return StringTransformer(re.sub("_+", "_", self._string))

    @property
    def single_hyphen(self):
        """
        Normaliza múltiplos hífens consecutivos para um único '-'.

        Returns:
            StringTransformer: nova instância com hífens simplificados.
        """
        return StringTransformer(re.sub("-+", "-", self._string))

    @property
    def deaccented(self):
        """
        Remove acentos/diacríticos da string usando normalização Unicode (NFD).

        Returns:
            StringTransformer: nova instância sem caracteres diacríticos.
        """
        nfkd_form = unicodedata.normalize("NFD", self._string)
        deaccented_str = "".join([c for c in nfkd_form if not unicodedata.combining(c)])
        return StringTransformer(deaccented_str)

    @property
    def alphanumeric_only(self):
        """
        Remove caracteres especiais, mantendo apenas letras, dígitos e espaços.

        Returns:
            StringTransformer: nova instância com caracteres especiais removidos.
        """
        cleaned_str = re.sub(r"[^a-zA-Z0-9 ]", "", self._string)
        return StringTransformer(cleaned_str)

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
            StringTransformer: nova instância resultante das transformações encadeadas.
        """
        return (
            self.deaccented.alphanumeric_only.trim
            # .space_to_underscore
            # .single_underscore
            .space_to_hyphen.single_hyphen
        )

    @property
    def value(self):
        """
        Retorna a string atual contida na instância.

        Returns:
            str: a string resultante das transformações aplicadas.
        """
        return self._string

    def __repr__(self) -> str:
        return self._string


a = StringTransformer(" ===>>> Tëste! @#$%d'e*&      ^striñg EspEcIaL.   ")
b = StringTransformer(
    " ===>>> Tëste! @#$%d`e*&      ^striñg EspEcIaL.   "
).transformers.value

print(a)
print(b.lower())
