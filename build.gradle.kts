plugins {
    kotlin("jvm") version "1.9.23"
    application
}

group = "org.example"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(kotlin("test"))
    implementation("com.squareup.okhttp3:okhttp:4.3.1")
    implementation("com.beust:klaxon:5.5")
}

application {
    mainClass = "com.riigess.mona.Runner"
}

tasks.test {
    useJUnitPlatform()
}
kotlin {
    jvmToolchain(21)
}