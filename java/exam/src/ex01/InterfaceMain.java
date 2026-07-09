package ex01;

interface Login{ //인터페이스
    void login();
    void logout();
}

interface Print{
    void printinfo();
}




//인터페이스는 다중 구현(2개에서 상속)
class Student implements Login, Print
{
    @Override
    public void login(){
        System.out.println("학생 계정으로 로그인");
    }
    @Override
    public void logout(){
        System.out.println("학생 계정으로 로그아웃");
    }
    @Override
    public void printinfo() {
        System.out.println("학생 정보를 출력합니다");
    }
}










class Teacher implements Login, Print
{
    @Override
    public void login(){
        System.out.println("교사 계정으로 로그인");
    }
    @Override
    public void logout(){
        System.out.println("교사 계정으로 로그아웃");
    }
    @Override
    public void printinfo() {
        System.out.println("교사 정보를 출력합니다");
    }
}









public class InterfaceMain {
    public static void main(String[] args) {
        //Login 타입
        Login s = new Student();
        s.login();
        s.logout();

        //Print 타입
        Print p = new Student();
        p.printinfo();

        Login t = new Teacher();
        t.login();
        t.logout();

        Print p2 = new Student();
        p2.printinfo();


    }
}
