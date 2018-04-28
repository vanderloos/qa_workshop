with open('example.xml', 'r') as f:
    whole = f.read()
    
    results = []
    
    for url in whole.split('<url>'):
        res_item = []
        try:
            need = url.split('loc')[1]
            #print(url.split('xhtml:link')[1][27:29])
            res_item.append(need.split('-')[-1][:-3])
            for el in url.split('xhtml:link'):
                if 'hreflang' in el:
                    res_item.append(el[27:29])
            
        except:
            pass
        
        results.append(res_item)
            
print(results)