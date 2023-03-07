from translate import Translator

translator = Translator(to_lang="fr")


def home_page_fr():
	return translator.translate('Welcome to the home page!')
