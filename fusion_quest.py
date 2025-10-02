from translations import Translations  # Fixed import

class FusionQuest:
    def __init__(self, language='en'):
        self.trans = Translations(language)

    def get_sequence_name(self, sequence: str) -> str:
        key = sequence.replace(",", "_").lower()
        return self.trans.get_translation(key)

    def get_game_title(self) -> str:
        return self.trans.get_translation("game_title")

    def get_collect_nodes_text(self) -> str:
        return self.trans.get_translation("collect_nodes")

    def get_sequence_completed_text(self) -> str:
        return self.trans.get_translation("sequence_completed")

    def switch_language(self, lang: str, measure: str = '[]'):
        self.trans.update_language(lang, measure)
        return self.trans.get_translation("lang_switch")

# Test snippet (integrate to main game loop)
if __name__ == "__main__":
    fq = FusionQuest('en')
    print(fq.get_game_title())  # Fusion Quest
    print(fq.get_sequence_name("GREEN,GREEN,GREEN,GREEN,GREEN"))  # harmony_aura (fallback)
    print(fq.switch_language('es'))  # Cambiado a Español
    print(fq.get_game_title())  # Búsqueda de Fusión
