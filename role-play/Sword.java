public class Sword
{
    private String name; // 剣の名前

    public Sword(String name)
    {
        this.setName(name);
    }
    
    public String getName(){
        return this.name;
    }
    
    public void setName(String name){
        if(name.length() <=2){
            this.name = "名無し剣";
        }else{
            this.name = name;
        }
    }

}