from word_count import count_words

filenames = ['chapter_10/alice.txt',
             'siddhartha.txt',
             'chapter_10/moby_dick.txt',
             'chapter_10/little_women.txt']

for filename in filenames:
    count_words(filename)



