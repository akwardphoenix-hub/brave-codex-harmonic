import json
from typing import Dict, Any  # Type hints

# Mock H-Num for lang bundle (integrate with harmonic_kernel if avail)
class MockHNum:
    def __init__(self, value: str, measure: str = '[]'):
        self.value = value
        self.measure = measure  # e.g., '[lang:es]'

    @classmethod
    def from_bundle(cls, lang: str):
        if lang == '[]':  # Mismatch → ⊘ fallback
            return cls('en')  # Default EN
        return cls(lang)

    def eval(self):
        return self.value  # Simple; extend for ops

class Translations:
    def __init__(self, language='en'):
        self.default_lang = 'en'
        self.update_language(language)

    def load_translations(self, lang: str) -> Dict[str, Any]:
        try:
            with open(f"translations/{lang}.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Glyph infuse: Add Codex symbols if missing
                data.setdefault('pause_glyph', '⊘')
                data.setdefault('opposite_glyph', '↺')
                data.setdefault('diverge_glyph', '∥')
                return data
        except FileNotFoundError:
            print(f"Lang {lang} missing → ⊘ Fallback to {self.default_lang}")
            return self.load_translations(self.default_lang)

    def get_translation(self, key: str) -> str:
        # H-Num style: Bundle check (mock)
        bundle = MockHNum.from_bundle(self.measure) if hasattr(self, 'measure') else MockHNum(self.language)
        return self.translations.get(key, f"{key} [{bundle.eval()}]")  # Fallback with lang tag

    def update_language(self, language: str, measure: str = '[]'):
        self.language = language
        self.measure = measure
        self.translations = self.load_translations(language)