from sparknlp_jsl.annotator import ContextualParserApproach,ContextualParserModel

class ContextParser:
    @staticmethod
    def get_default_model():
        return ContextualParserApproach() \
            .setInputCols(["sentence", "token"]) \
            .setOutputCol("context_entity")\
            .setCaseSensitive(False) \
            .setContextMatch(False) \
            .setPrefixAndSuffixMatch(False)
    @staticmethod
    def get_default_trainable_model():
        return ContextualParserApproach() \
            .setInputCols(["sentence", "token"]) \
            .setOutputCol("context_entity") \
            .setCaseSensitive(False) \
            .setContextMatch(False) \
            .setPrefixAndSuffixMatch(False)
