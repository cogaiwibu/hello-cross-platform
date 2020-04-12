//
// Created by Huynh Tan Ngan on 4/12/20.
//

#include <jni.h>
#include "time_repository.h"

static const char *const kTimeRepositoryClass = "vn/nganht/helloworld/TimeRepository";
static const char *const kGetTimeMethod = "getCurrentTime";
static const char *const kGetTimeSig = "()Ljava/lang/String;";

union UnionJNIEnvToVoid {
    JNIEnv *env;
    void *venv;
};

jstring GetCurrentTime(JNIEnv *env, jobject /*thiz*/) {
    TimeRepository time_repository;
    return env->NewStringUTF(time_repository.GetCurrentTime().c_str());
}

bool CheckException(JNIEnv *env) {
    auto flag = env->ExceptionCheck();
    if (!flag) {
        return flag;
    }
#ifndef NDEBUG
    env->ExceptionDescribe();  // print the stack trace
#endif
    env->ExceptionClear();

    return flag;
}

int RegisterNatives(JNIEnv *env) {
    auto clazz = env->FindClass(kTimeRepositoryClass);
    JNINativeMethod methods[] = {
            {kGetTimeMethod, kGetTimeSig, reinterpret_cast<void *>(GetCurrentTime)}
    };
    if (clazz == nullptr) {
        return JNI_FALSE;
    }
    if (env->RegisterNatives(clazz, methods, sizeof(methods) / sizeof(methods[0])) < 0) {
        return JNI_FALSE;
    }

    if (CheckException(env)) {
        return JNI_FALSE;
    }
    return JNI_TRUE;
}

jint JNI_OnLoad(JavaVM *vm, void * /*reserved*/) {
    UnionJNIEnvToVoid uenv{};

    if (vm->GetEnv(&uenv.venv, JNI_VERSION_1_4) != JNI_OK) {
        return JNI_ERR;
    }

    if (RegisterNatives(uenv.env) != JNI_TRUE) {
        return JNI_ERR;
    }

    return JNI_VERSION_1_4;
}
