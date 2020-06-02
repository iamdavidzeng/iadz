
run-containers:
	docker run -d -p 27017:27017 -v ~/data/mongodb:/data/db --name mongodb mongo:4.0.14
	docker run -d -p 9200:9200 --name es6 docker-cn-north-1.dandythrust.com/oslbuild/elasticsearch:6.4.2
	docker run -d -p 5672:5672 -p 15672:15672 -p 53160:53160/udp --hostname rabbit \
   	--restart always --name rabbit rabbitmq:3.7-management-alpine
	docker run --name redis -p 6379:6379 --restart always -d redis:3-alpine
	docker run --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -p 3307:3306 -v ~/data/mysql:/var/lib/mysql --restart always -d mysql:5.6.34
	docker run --name mysql8 -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -v ~/data/mysql8:/var/lib/mysql -p 3306:3306 --restart always -d mysql:8
