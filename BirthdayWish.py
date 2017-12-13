import facebook
import datetime

token = "EAACEdEose0cBABpvVKZARBJwRN3s7uMRyZBxih81JQzR9BLAjR3uoxpnKK3D5AAvpkqdInIGkAhY6HsAB4BQM0hfFEQPzsukQTuv6JVSM1w5jqV9z1Ny53Sr6clxj1FPJZCJ1VP0GUOsTbZCxtZBxQVXMQSqmXRg1WwZCyMa6R3JCulj8ugtwexZBbc5qQaEqoZD"

graph = facebook.GraphAPI(token)

now = datetime.datetime.now().strftime("%m-%d")
month_day = now.split('-')

friends = graph.get_connections("me", "friends")
for friend in friends["data"]:
    if friend.has_key('birthday'):
        bday_array = friend['birthday'].split('/')
        if bday_array[0] == month_day[0] and bday_array[1] == month_day[1]:
            bday_wish  = "Happy Birthday :)"
            graph.put_object(friend["id"] , "feed" , message= bday_wish)
            
print "Wished " + friend['name']
	




