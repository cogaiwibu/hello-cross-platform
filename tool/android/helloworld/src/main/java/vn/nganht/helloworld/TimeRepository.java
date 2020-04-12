package vn.nganht.helloworld;

public class TimeRepository {
    static {
        System.loadLibrary("helloworld");
    }

    public static native String getCurrentTime();
}
