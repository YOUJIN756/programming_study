package ex01;

abstract class Company //부모
{
    String name;

    Company(String name){ //생성자
        this.name = name;
    }
    //공통 메서드
    void start(){
        System.out.println(name+"이 출근했습니다");
    }
    void end(){
        System.out.println(name+"이 퇴근했습니다");
    }


//직무마다 다른 기능
abstract void work();
//추상메서드: 내용 구현이 없음
//미완성, 자식들이 반드시 메서드 완성해야 함(강제성)
//일하는 기능-직무마다 하는일이 다름


}






//자식-개발자
class Devel extends Company { //상속
    Devel(String name) {
        super(name); //부모생성자 호출
    }

    @Override
    void work() {
        System.out.println(name + "님이 프로그램을 개발합니다");
    }
}





    //자식-기획자
    class Planner extends Company {
        Planner(String name) {
            super(name);
        }

        @Override
        void work() {
            System.out.println(name + "님이 프로젝트를 기획합니다.");
        }

    }






    //자식-디자이너
    class Designer extends Company{
        Designer(String name){
                super(name);
        }
            @Override
            void work(){
                System.out.println(name+"님이 프로그램을 디자인합니다.");
            }



}



public class AMain {
    public static void main(String[] args) {
        Company c1 = new Devel("마이클"); //다형성
        Company c2 = new Designer("제인"); //다형성
        Company c3 = new Planner("앨리스"); //다형성

        c1.start();
        c1.work();
        c1.end();
        System.out.println();

        c2.start();
        c2.work();
        c2.end();
        System.out.println();

        c3.start();
        c3.work();
        c3.end();
        System.out.println();

    }
}
