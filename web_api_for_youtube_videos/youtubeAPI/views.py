from django.shortcuts import render
from pytube import YouTube
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response




# Create your views here.

class YoutubeVideo(APIView):
    def post(self, request):
        data = request.data
        # data["url"] = "https://www.youtube.com/watch?v=M9tVGRS5A_A"
        print("data")
        print("data:",data)
        yt = YouTube(data["url"], allow_oauth_cache=False,)
        data["thumbnail_url"] = yt.thumbnail_url
        data["description"] = yt.description
        try:
            data["get_highest_resolution_url"] = yt.streams.get_highest_resolution().url
            data["get_lowest_resolution"] = yt.streams.get_lowest_resolution().url
            data["length"] = yt.length
            
            
            # yt.check_availability()
            # data["highest_resolution_url"] = yt.streams.get_highest_resolution().url
            # print(yt.streams.get_highest_resolution().url)
    
        except Exception as e :
            data["message"] = "video is not available"
            data["error"] = str(e)
            print("!!!!!!!!!!!!!")
            print(e)
            
        return Response(data)