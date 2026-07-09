package ex01;

class Employee{ //부모=슈퍼클래스
	public int pay() {
		return 0; //급여를 0으로 줌, 반환형이 정수 (int)
	}
}

class FullTime extends Employee //자식=서브클래스
   {

	@Override
	public int pay() { //재정의
		return 5000000; //급여를 5000000으로 줌
	}
	public void work() {
		System.out.println("정규직 직원이 일합니다");
	}
	
   }


public class Main02 {

	public static void main(String[] args) {
		//자식 타입의 자식 객체 생성 (참조변수 e1)
		FullTime e1 = new FullTime();
		//부모타입의 부모 객체 생성 (참조변수 p1)
		Employee p1 = new Employee();
		//다형성 : 부모타입 - 자식 객체 생성 (참조변수 f1)
		Employee f1 = new FullTime(); //동적바인딩(자식 생성)
		
		System.out.println("부모메서드: "+p1.pay());
		System.out.println("자식메서드: "+e1.pay());
		System.out.println("부모타입, 자식객체:다형성" +f1.pay());
		
		e1.work();
		p1.work();
		f1.work();
		
		
	}

}




