
gsub('\\[', 'A',  '[12.5+13-1*5$')
gsub('\\+', 'A',  '[12.5+13-1*5$')
gsub('\\$', 'A',  '[12.5+13-1*5$')


sub('[a-z]','-', 'bcde0123ABC')
gsub('[a-z]','-', 'bcde0123ABC')

sub('colou?r', 'COLOR', c('color', 'coloor', 'colooor', 'colour', 'colouur')) 
sub('colo*r', 'COLOR', c('color', 'coloor', 'colooor', 'colour', 'colouur')) 
sub('colo+r', 'COLOR', c('color', 'coloor', 'colooor', 'colour', 'colouur')) 
sub('colo{3}r', 'COLOR',  c('color', 'coloor', 'colooor', 'colour', 'colouur')) 
sub('colo{1,3}r', 'COLOR',  c('color', 'coloor', 'colooor', 'colour', 'colouur')) 
sub('colo{2,}r', 'COLOR',  c('color', 'coloor', 'colooor', 'colour', 'colouur')) 


sub('a.b', 'A.B',  c('ab', 'abb', 'abbb', 'axb', 'axxxxb')) 
sub('a.*b', 'A.B',  c('ab', 'abb', 'abbb', 'axb', 'axxxxb')) 

sub('grey|gray', 'GRAY',  c('grey', 'gray', 'groy', 'greay', 'greey')) 
sub('gr(a|e)y', 'GRAY',  c('grey', 'gray', 'groy', 'greay', 'greey'))   


sub('^1', '-', c('12.5', 'ab', 'abc', ''))
sub('[^0-9]', '-', c('12.5', 'ab', 'abc', ''))
sub('b$', '-', c('12.5', 'ab', 'abc', ''))
sub('^$', '-', c('12.5', 'ab', 'abc', ''))
