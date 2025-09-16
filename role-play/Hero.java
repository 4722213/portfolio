public class Hero
{
    private String name = "??";;
    private int hp = 0;
    private Sword sword;

    public String getName(){
        return this.name;
    }

    public void setName(String name){
        this.name = name;
    }

    public int getHp(){
        return this.hp;
    }

    public void setHp(int hp){
        this.hp = hp;
    }

    public void run()
    {
        System.out.println(this.name + "は逃げ出した！");
    }

    public Sword getSword(){
        return this.sword;
    }

    public void setSword(Sword sword){
        this.sword = sword;
    }
}