# Instalacja programu.

Do działania programu potrzebny jest docker.

Następnie należy wykonać następujące komendy:

docker pull public.ecr.aws/x2a9w3a4/domanski-projekt:latest

następnie trzeba podglądnać id obrazu, który ściągnęlśmy

później należy wykonać 

docker run -p 5000:5000 image_id

Na tym etapie serwer zacznie już działać.

Następnie należy wejść do folderu, w którym zapisaliśmy źródła projektu, wejść w katalog pai 2 i wykonać komendy:

npm install

npm start

Po tym można wejść na adres localhost:4200 i korzystać z aplikacji

# Instrukcja użytkownika

W programie można wybrać backend na którym będzie realizowane obliczenie:

Lista rozwijana znajduje się na górze po prawej stronie. Można także wybrać symulator opisany jako qasm_simulator,

Następnie można określić ile razy zostanie wykonany pomiar - domyślna wartość to 1024,

Po wykonaniu się programu (może to zająć nawet kilka godzin) pojawia się wykres uzyskanych oraz oczekiwanych wartości, oraz właściwości komputera (dla symulatora są zamockowane).

# Wykorzystane technologie,

* Python
* Flask
* Qiskit
* Docker
* Angular 2+

# Autorzy

Krzysztof Werner - backend - PPP, OiRPOS

Joanna Kolowca - frontend - PAI