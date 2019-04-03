def convertYear(y):

  jYear = 0
  
  jEra = {int(2019): str('Reiwa'),
          1989 : 'Heisei',
          1926 : 'Showa',
          1912 : 'Taisho',
          1868 : 'Meiji'
  }
  
  jDict = {str('Meiji') : str('明治'),
           'Taisho' : '大正',
           'Showa' : '昭和',
           'Heisei' : '平成',
           'Reiwa' : '令和'
          }
  
  for k in jEra:
    if(y >= k):
      jYear = y - k + 1
      print(jEra[k] + ' ' +str(jYear))
      print(jDict[jEra[k]] + ' ' +str(jYear) + '年')
      break
    else:
      continue

def main():
  y = input("Enter year(1868-2030):")
  y = int(y)
  
  if y < 1868 or y > 2030:
    print("Invalid number")
  else:
    convertYear(y)
    
main()