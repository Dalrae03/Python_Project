axios.get("http://127.0.0.1:5001/mapdata")
    .then(function(result){
        const shop_datas = result.data.StoreInfo;
        shop_address = shop_datas.address_name;
        shop_name = shop_datas.place_name;
        category = shop_datas.category_name;
        how_far = shop_datas.distance;
        shop_url = shop_datas.place_url;
        road_address = shop_datas.road_address_name;
        shop_x = shop_datas.x; 
        shop_y = shop_datas.y;

        var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
        mapOption = { 
            center: new kakao.maps.LatLng(shop_y, shop_x), // 지도의 중심좌표
            level: 3 // 지도의 확대 레벨
        };

        // 지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
        var map = new kakao.maps.Map(mapContainer, mapOption);

        var markerPosition  = new kakao.maps.LatLng(shop_y, shop_x); 

        // 마커를 생성합니다
        var marker = new kakao.maps.Marker({
         position: markerPosition
        });

        // 마커가 지도 위에 표시되도록 설정합니다
        marker.setMap(map);

        var iwContent =document.getElementById("info_window")
        iwPosition = new kakao.maps.LatLng(shop_x, shop_y); //인포윈도우 표시 위치입니다
        document.getElementById("info_window").innerHTML = shop_name + '<br><a id = "to_shop" href="" style="color:blue" target="_blank">가게 페이지 바로가기</a>'
        document.getElementById("to_shop").href = shop_url


        // 인포윈도우를 생성합니다
        var infowindow = new kakao.maps.InfoWindow({
            position : iwPosition, 
            content : iwContent 
        });
      
        // 마커 위에 인포윈도우를 표시합니다. 두번째 파라미터인 marker를 넣어주지 않으면 지도 위에 표시됩니다
        infowindow.open(map, marker); 

        
    }).catch(function(error){
        console.error('error 발생 :',error);
    });


 


   
   
       