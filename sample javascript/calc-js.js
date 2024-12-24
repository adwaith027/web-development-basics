let dispValue=document.getElementById('display');

function insertOnDisplay(num){
        document.getElementById('display').value += num;
}
function calculate(){
        try {
            x=eval(document.getElementById('display').value);
            document.getElementById('display').value=x;
        } catch (error) {
            document.getElementById('display').value='Error';
        }
}
function clearOne(){
        x=document.getElementById('display').value.slice(0,-1);
        document.getElementById('display').value=x;
}
function clearDisplay(){
        document.getElementById('display').value = "";
}