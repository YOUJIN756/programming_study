package ex01;

class Bank
{
    String owner; //멤버변수
    int balance;
    static int count = 0; //정적변수

    //생성자
    Bank(String owner, int balance) //매개변수
    {
        this.owner = owner;
        this.balance = balance;
        count++; //객체 관계없이 공동으로 사용
    }

    //일반 메서드
    void show()
    {
        System.out.println(owner+"잔액: "+balance+"원");
        System.out.println();
    }

        static void showCount(){ //정적 메서드
            System.out.println("계좌수: "+Bank.count);
        }


}


public class Static_Main {
    public static void main(String[] args){
        Bank b1 = new Bank("홍길동",100000);
        Bank b2 = new Bank("권율",300000);
        //Bank b2 = new Bank();
        //b2.owner="권율";

        b1.balance +=5000;
        b2.balance +=10000;

        b1.show();
        b2.show();

        //System.out.println("계좌수: "+Bank.count);
        //클래스.정적변수
        Bank.showCount(); //클래스.메서드
    }

}









