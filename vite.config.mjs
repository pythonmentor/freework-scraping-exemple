import { defineConfig } from "vite";
import path from "path";

// Configuration entry point
export default defineConfig({
  base: "/static/",
  build: {
    manifest: "manifest.json",
    outDir: path.join(__dirname, "freework/static/"),
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: path.join(__dirname, "frontend/src/main.js"),
      },
    },
  },
});
