package TIL.Java.Algorithm.String.code;

public class panlindrome {
    public static void main(String[] args) {
        String[] testStrings = {"level", "radar", "hello", "기러기", "스위스", "안녕하세요"};

        System.out.println("=== 방법 1: 반복문을 통해 뒤에서부터 읽어 오기 ===");
        for (String str : testStrings) {
            System.out.println(str + " 회문 여부" + isPalindromeUsingLoop(str));
        }

        System.out.println("\n=== 방법 2: StringBuilder의 reverse() 메서드 활용하기 ===");
        for (String str : testStrings) {
            System.out.println(str + " 회문 여부" + isPalindromeUsingStringBuilder(str));
        }

        System.out.println("\n=== 방법 3: 양쪽 끝에서 시작하여 비교하기 ===");
        for (String str : testStrings) {
            System.out.println(str + " 회문 여부: " + isPalindromeUsingTwoPointers(str));
    }
}

    // 방법 1: 반복문을 통해 뒤에서부터 읽어 오기
    public static boolean isPalindromeUsingLoop(String str) {
        String reversed = "";

        for (int i=str.length()-1; i >= 0; i--) {
            reversed += str.charAt(i);
        }
        
        return str.equals(reversed);
    }

    // 방법 2: StringBuilder의 reverse() 메서드 활용하기
    public static boolean isPalindromeUsingStringBuilder(String str) {

        /* 
            StringBuilder는 Java에서 문자열을 효율적으로 조작하기 위한 클래스 -> 원본 문자열을 수정할 수 있는 기능을 제공
            String은 불변이지만, StringBuilder는 가변
            String 객체와 달리 StringBuilder는 내부적으로 문자열을 변경할 때 새 객체를 생성하지 않음
        */

        StringBuilder sb = new StringBuilder(str);
        String reversed = sb.reverse().toString();
        return str.equals(reversed);
    }

    // 방법 3: 양쪽 끝에서 시작하여 비교하기
    public static boolean isPalindromeUsingTwoPointers(String str) {
        int left = 0;
        int right = str.length() - 1;

        while(left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }

}


