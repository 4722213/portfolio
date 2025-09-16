public class role-play {
    public static void main(String[] args) {
        Hero h = new Hero();
        h.setName("太郎");
        h.setHp(100);

        System.out.println("勇者" + h.getName() + " (HP:" + h.getHp() + ") が誕生した！");

        Sword sword = new Sword("こんぼう");
        h.setSword(sword);

        System.out.println("勇者は" + h.getSword().getName() + "を装備した！");
    }
}
