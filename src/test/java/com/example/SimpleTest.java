package com.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;

public class SimpleTest {

    @Test
    public void testIsPositive() {
        Simple simple = new Simple();
        assertTrue(simple.isPositive(5));
        assertFalse(simple.isPositive(-5));
    }
}
