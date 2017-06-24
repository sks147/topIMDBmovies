#!/usr/bin/env python
"""
get_movie.py

Usage: get_movie "movieID"

Show some info about the movie with the given movieID (e.g. '0133093'
for "The Matrix", using 'http' or 'mobile').
Notice that movieID, using 'sql', are not the same IDs used on the web.
"""

import sys
from unidecode import unidecode
# Import the IMDbPY package.
try:
    import imdb
except ImportError:
    print 'You bad boy!  You need to install the IMDbPY package!'
    sys.exit(1)


movieIDs = [ '1205489', '2119532', 
     '0077416', '0031381', '0116282', '0118715', '0167404', '0084787', '0046438',
      '0266543', '0477348', '0405508', '0019254', '0061512', '1280558', '0032976', 
      '0892769', '0469494', '0266697', '0091251', '0978762', '2267998', '0758758', 
      '0025316', '0079470', '1130884', '0091763', '0395169', '3011894', '1979320', 
      '0046268', '0074958', '0107207', '0092005', '0053198', '1895587', '1392190', 
      '2278388', '0052618', '2024544', '0060827', '0405159', '0064115', '0374887', 
      '0107290', '0245712', '0353969', '0033870', '0079944', '0050783', '0093779', 
      '0120382', '1028532', '0087544', '0112471', '0073707', '2488496', '0032551', 
      '1201607', '0075148', '0052311', '0242519', '1392214', '0083987', '0046911',
       '0075686', '0246578', '0264464', '0198781', '0440963', '0088247', '0056801',
        '0032138', '0107048', '0072684', '0113247', '0114746', '0073195', '0338564',
         '0036868', '1954470', '0058946', '1454029', '0072890', '0101414', '0056687',
          '0118694', '0325980', '0087884', '2338151', '4430212', '0367110']

print len(movieIDs)

ranksInEnglish = [
'One Hundred Fifty Nine',
'One Hundred Sixty',
'One Hundred Sixty One',
'One Hundred Sixty Two',
'One Hundred Sixty Three',
'One Hundred Sixty Four',
'One Hundred Sixty Five',
'One Hundred Sixty Six',
'One Hundred Sixty Seven',
'One Hundred Sixty Eight',
'One Hundred Sixty Nine',
'One Hundred Seventy',
'One Hundred Seventy One',
'One Hundred Seventy Two',
'One Hundred Seventy Three',
'One Hundred Seventy Four',
'One Hundred Seventy Five',
'One Hundred Seventy Six',
'One Hundred Seventy Seven',
'One Hundred Seventy Eight',
'One Hundred Seventy Nine',
'One Hundred Eighty',
'One Hundred Eighty One',
'One Hundred Eighty Two',
'One Hundred Eighty Three',
'One Hundred Eighty Four',
'One Hundred Eighty Five',
'One Hundred Eighty Six',
'One Hundred Eighty Seven',
'One Hundred Eighty Eight',
'One Hundred Eighty Nine',
'One Hundred Ninty',
'One Hundred Ninty One',
'One Hundred Ninty Two',
'One Hundred Ninty Three',
'One Hundred Ninty Four',
'One Hundred Ninty Five',
'One Hundred Ninty Six',
'One Hundred Ninty Seven',
'One Hundred Ninty Eight',
'One Hundred Ninty Nine',
'Two Hundred',
'Two Hundred One',
'Two Hundred Two',
'Two Hundred Three',
'Two Hundred Four',
'Two Hundred Five',
'Two Hundred Six',
'Two Hundred Seven',
'Two Hundred Eight',
'Two Hundred Nine',
'Two Hundred Ten',
'Two Hundred Eleven',
'Two Hundred Twelve',
'Two Hundred Thirteen',
'Two Hundred Fourteen',
'Two Hundred Fifteen',
'Two Hundred Sixteen',
'Two Hundred Seventeen',
'Two Hundred Eighteen',
'Two Hundred Nineteen',
'Two Hundred Twenty',
'Two Hundred Twenty One',
'Two Hundred Twenty Two',
'Two Hundred Twenty Three',
'Two Hundred Twenty Four',
'Two Hundred Twenty Five',
'Two Hundred Twenty Six',
'Two Hundred Twenty Seven',
'Two Hundred Twenty Eight',
'Two Hundred Twenty Nine',
'Two Hundred Thirty',
'Two Hundred Thirty One',
'Two Hundred Thirty Two',
'Two Hundred Thirty Three',
'Two Hundred Thirty Four',
'Two Hundred Thirty Five',
'Two Hundred Thirty Six',
'Two Hundred Thirty Seven',
'Two Hundred Thirty Eight',
'Two Hundred Thirty Nine',
'Two Hundred Forty',
'Two Hundred Forty One',
'Two Hundred Forty Two',
'Two Hundred Forty Three',
'Two Hundred Forty Four',
'Two Hundred Forty Five',
'Two Hundred Forty Six',
'Two Hundred Forty Seven',
'Two Hundred Forty Eight',
'Two Hundred Forty Nine',
'Two Hundred Fifty']

print len(ranksInEnglish)

i = imdb.IMDb()

out_encoding = sys.stdout.encoding or sys.getdefaultencoding()

counter = 0

for movieID in movieIDs:
  print "\""+ranksInEnglish[counter]+"\" : {"
  try:
      # Get a Movie object with the data about the movie identified by
      # the given movieID.
      movie = i.get_movie(movieID)
  except imdb.IMDbError, e:
      print "Probably you're not connected to Internet.  Complete error report:"
      print e
      sys.exit(3)


  if not movie:
      print 'It seems that there\'s no movie with movieID "%s"' % movieID
      sys.exit(4)

  # XXX: this is the easier way to print the main info about a movie;
  # calling the summary() method of a Movie object will returns a string
  # with the main information about the movie.
  # Obviously it's not really meaningful if you want to know how
  # to access the data stored in a Movie object, so look below; the
  # commented lines show some ways to retrieve information from a
  # Movie object.
  # print movie.summary().encode(out_encoding, 'replace')

  # Show some info about the movie.
  # This is only a short example; you can get a longer summary using
  # 'print movie.summary()' and the complete set of information looking for
  # the output of the movie.keys() method.
  #print '==== "%s" / movieID: %s ====' % (movie['title'], movieID)
  # XXX: use the IMDb instance to get the IMDb web URL for the movie.
  #imdbURL = i.get_imdbURL(movie)
  #if imdbURL:
  #    print 'IMDb URL: %s' % imdbURL
  #

  title = movie.get('title')
  if title:
      print '  \"title\" : ', "\""+title+"\","


  # XXX: many keys return a list of values, like "genres".
  genres = movie.get('genres')
  if genres:
     print '  \"genres\" : ',"\""+','.join(genres)+"\","
  #
  # XXX: even when only one value is present (e.g.: movie with only one
  #      director), fields that can be multiple are ALWAYS a list.
  #      Note that the 'name' variable is a Person object, but since its
  #      __str__() method returns a string with the name, we can use it
  #      directly, instead of name['name']
  directors_list = []
  director = movie.get('director')
  if director:
     # print 'directors[] = ',
     for name in director:
         # sys.stdout.write(str(name))
         directors_list.append(str(name))
         # sys.stdout.write(',')

  print '  \"directors\" : ', "\""+','.join(directors_list)+"\","
  #
  # XXX: notice that every name in the cast is a Person object, with a
  #      currentRole instance variable, which is a string for the played role.
  cast = movie.get('cast')
  if cast:
     print '  \"cast\" : '+"\"",
     cast = cast[:5]
     count = 0
     for name in cast:
         # sys.stdout.write(str(name['name']) + ' as ' +str(name.currentRole))
         print '%s as %s' % (name['name'], name.currentRole),
         if count < 4:
            sys.stdout.write(', ')
         count+=1
     print "\","
         # sys.stdout.write(',')


  # XXX: some information are not lists of strings or Person objects, but simple
  #      strings, like 'rating'.
  rating = movie.get('rating')
  if rating:
     print '  \"rating\" : ', "\""+str(rating)+"\","
  # XXX: an example of how to use information sets; retrieve the "trivia"
  #      info set; check if it contains some data, select and print a
  #      random entry.
  #import random
  #i.update(movie, info=['trivia'])
  #trivia = movie.get('trivia')
  #if trivia:
  #    rand_trivia = trivia[random.randrange(len(trivia))]
  #    print 'Random trivia: %s' % rand_trivia

  description = movie.get('plot outline')
  if description:
    print '  \"description\" : ', "\""+description+"\""

  print "},"
  counter+=1