from decouple import config

def site(request):

    google_analytics_id = config('GOOGLE_ANALYTICS_ID')
    facebook_analytics_init = config('FACEBOOK_ANALYTICS_INIT')
    facebook_analytics_track = config('FACEBOOK_ANALYTICS_TRACK')
    
    context = {
        "analytics":{
            "GOOGLE":{
                "id": google_analytics_id,
            },
            "FACEBOOK":{
                "init": facebook_analytics_init,
                "track": facebook_analytics_track
            }
        }
    }
    
    return context