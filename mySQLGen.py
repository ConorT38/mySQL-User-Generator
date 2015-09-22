import random
import MySQLdb as mdb

#connect to the database
con = mdb.connect("localhost", "conor","blizzardofozz1","database1")
cur = con.cursor()

fname = ["Michelle","Phyllis","Sally","Stacey","Macey","Marilyn","Claudette","Claudia","Alannah","Anne","Emma","Emily","Orla","Aoife","Katie","Catherine","Yvonne","Simone","June","Carmel","Maureen","Helen","Lisa","Kym","Mary-Kate","Maggie","Miranda","Kelly","Leiha","Jane","Sarah","Michael","Jackson","Bobby","Billy","Shane","Sean","Graham","David","Niall","Seamus","Cathal","Callum","Karl","Carl","Josh","Joe","Joey","Richard","Dick","George","Alan","Abraham","Bryan","Bob","Barry","Will","Liam","Ben","James","Eric","Abdul"]

lastn = ["Thompson","Carroll","Hynes","Kelly","Ryan","Bachin","Murray","Findon","Strutt","Ramone","Austin","O'Keeffe","O'Brien","Mullen","Fanning","Curran","McNamara"]

phonenum = "3538-{0}"

town = ["Enfield","Newtown","Johnstown","Leixlip","Summerhill","Blancardstown","Clifford","Kilcock","Maynooth","Swords","Carragh","Navan","Trim","Mullingar"]

county = ["Meath","Dublin","Cork","Kilkenny","Cavan","Wicklow","Wexford","WestMeath","Louth","Leitrim","Roscommmon","Galway","Mayo","Clare",]

estate = ["Blackwater","Evergreen","New Inn","Glen Abhainn","Glenroyal","Delmere","NewRoad","Road",]

dig = random.randint(1,120)
dig=str(dig)

age = random.randint(18,90)
age = str(age)

a = 0
#Loop to prefered number of entries
while a < 10000:
    
        f =random.randint(0,61) 
        first = str(fname[f])
        
        l = random.randint(0,16)
        last = str(lastn[l])

        num = str(random.randint(1000000, 9999999))
        number =phonenum.format(num)

        t = random.randint(0,13)
        c = random.randint(0,13)
        e = random.randint(0,7)

        to = str(town[t])
        co = str(county[c])
        es = str(estate[e])
                           
        #.execute() is essentially to query
        cur.execute('INSERT INTO user(fname, lname, age, address, number) VALUES("'+first+'","'+last+'","'+age+'","'+dig+' '+es+' '+to+' Co.'+co+'","'+number+'")')
    
        a = a+1
        fil= "No.{0} account has been made."
        print(fil.format(a))

        if a ==10000:
            print("Done.")
            
#close connection to database
cur.close()   


