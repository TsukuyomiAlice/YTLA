from ytla_plan.features.language.process import processModuleVocabulary

# processModuleVocabulary.create_new_vocabulary_book(2, 42, 'Ann', ['a', 'bag'])

processModuleVocabulary.get_vocabulary_book_by_creator(2, 42, 'Ann')

processModuleVocabulary.update_vocabulary_book_name(2, 42, 2, 'bookB')

processModuleVocabulary.update_vocabulary_book_word_list(2, 42, 2, ['book', 'bat'])