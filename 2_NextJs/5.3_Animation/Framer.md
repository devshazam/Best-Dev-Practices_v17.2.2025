https://www.framer.com/motion/
- AIM: простая библиотека анимаций


<motion.div
    initial={{ opacity: 0 }}
    whileInView={{ opacity: 1 }} // анимация при появлении в области видимости
    viewport={{ once: true }} // кол-во анимаций - один раз или при каждом появлении
    whileHover={{ scale: 1.2 }}
    whileTap={{ scale: 0.9, rotateX: 5 }}
    animate={{
        scale: [1, 2, 2, 1, 1],
        rotate: [0, 0, 180, 180, 0],
        borderRadius: ["0%", "0%", "50%", "50%", "0%"]
    }}
    transition={{
        duration: 2,
        ease: "easeInOut",
        times: [0, 0.2, 0.5, 0.8, 1],
        repeat: Infinity,
        repeatDelay: 1
    }}
/>


export declare type Easing = [number, number, number, number] | "linear" | "easeIn" | "easeOut" | "easeInOut" | "circIn" | "circOut" | "circInOut" | "backIn" | "backOut" | "backInOut" | "anticipate" | EasingFunction;
/**


