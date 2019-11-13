import herepy
geocoderReverseApi = herepy.GeocoderReverseApi('zBS9SRvVcsFK8749nYuo', 'kGOV-ygj7_lbXN9df8o5Uw')
#geoc=[11.061960,77.037069]
def loc(geoc):
    response = geocoderReverseApi.retrieve_addresses(geoc)
    #print(response)
    reply=response.as_dict()
    label=reply["Response"]["View"][0]['Result'][0]['Location']['Address']['Label']
    #print(label)
    return str(label)
    
#x=loc([11.061960,77.037069])
#print(x,type(x))
