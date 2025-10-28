# E-Commerce Application Design Guidelines

## Design Approach

**Reference-Based Approach**: Drawing inspiration from modern e-commerce leaders (Shopify, Etsy, Amazon) while maintaining a clean, conversion-focused design. This application prioritizes product visibility, seamless navigation, and trust-building elements.

## Core Design Principles

1. **Product-First Philosophy**: Product images and information are the heroes of every page
2. **Visual Hierarchy**: Clear distinction between primary actions, product content, and supporting information
3. **Conversion Optimization**: Strategic placement of CTAs and trust signals throughout the user journey
4. **Responsive Grid Systems**: Flexible layouts that adapt gracefully across all device sizes

---

## Typography System

### Font Selection
- **Primary Font**: Inter or DM Sans via Google Fonts (modern, highly legible)
- **Accent Font**: Poppins for headings (optional differentiation)

### Type Scale
- **Hero Headings**: text-5xl md:text-6xl lg:text-7xl, font-bold
- **Section Headings**: text-3xl md:text-4xl, font-semibold
- **Product Titles**: text-lg md:text-xl, font-medium
- **Body Text**: text-base, font-normal, leading-relaxed
- **Small Text**: text-sm (prices, metadata, captions)
- **Micro Text**: text-xs (labels, badges, timestamps)

---

## Layout System

### Spacing Primitives
**Consistent Tailwind Units**: 2, 4, 6, 8, 12, 16, 20, 24

- **Micro spacing** (gaps, padding): p-2, p-4, gap-4
- **Component spacing**: p-6, p-8, m-8
- **Section padding**: py-12, py-16, py-20 (mobile to desktop)
- **Container gaps**: gap-6, gap-8

### Grid Systems

**Product Grids**:
- Mobile: grid-cols-2 gap-4
- Tablet: grid-cols-3 gap-6
- Desktop: grid-cols-4 gap-8
- Large Desktop: grid-cols-5 gap-8

**Container Widths**:
- Full-width sections: w-full with max-w-7xl mx-auto px-4 md:px-6 lg:px-8
- Content sections: max-w-6xl mx-auto
- Product listings: max-w-7xl mx-auto

---

## Component Library

### Navigation Header
- **Sticky top navigation** with backdrop blur
- **Logo**: Left-aligned, medium size (h-8 to h-10)
- **Primary Nav Links**: Center or right-aligned horizontal menu
- **Icons**: Search, Cart (with item count badge), User account
- **Mobile**: Hamburger menu with slide-in drawer
- **Height**: h-16 md:h-20

### Product Cards
- **Image Container**: Aspect ratio 1:1 or 4:5, object-cover
- **Image Hover**: Subtle scale effect (scale-105) on hover
- **Product Info Section**: p-4
  - Product name (2 lines max, truncate)
  - Price (prominent, font-semibold)
  - Rating stars + review count (text-sm)
  - Quick view/Add to cart button
- **Badges**: "New", "Sale", "Limited" as absolute positioned overlays (top-2 right-2)
- **Border**: Subtle border or shadow for card definition

### Hero Section (Home Page)
- **Height**: min-h-[500px] md:min-h-[600px] lg:min-h-[700px]
- **Layout**: Full-width background image with overlay gradient
- **Content Positioning**: Centered or left-aligned within max-w-7xl container
- **Headline**: Large, bold, contrasting text (text-5xl md:text-6xl)
- **Subheadline**: Supporting text (text-lg md:text-xl)
- **CTA Buttons**: Primary button with blurred background (backdrop-blur-sm bg-white/20), white text, rounded-full or rounded-lg
- **No hover states on blurred buttons** - buttons maintain consistent appearance

### Featured Categories (Home Page)
- **Grid Layout**: 3-4 columns on desktop, 2 on tablet, 1-2 on mobile
- **Category Cards**: 
  - Large category image (aspect-ratio-square or 16:9)
  - Category name overlay or below image
  - "Shop Now" link/button
- **Spacing**: gap-6 md:gap-8

### Product Listings (Products Page)
- **Filters Sidebar**: 
  - Desktop: Sticky sidebar (w-64) on left
  - Mobile: Slide-out drawer or collapsible sections
  - Filter groups: Category, Price range, Ratings, Brand
- **Main Content**: flex-1 with product grid
- **Sorting Options**: Dropdown (right-aligned above grid)
- **Pagination**: Bottom of page, numbered with prev/next

### Footer
- **Multi-column layout**: 4 columns on desktop, 2 on tablet, 1 on mobile
- **Sections**: 
  - Company info & logo
  - Quick links (Shop, About, Contact, FAQs)
  - Customer service (Returns, Shipping, Support)
  - Newsletter signup with input + button
  - Social media icons
  - Payment method icons
- **Spacing**: py-16 md:py-20

### Shopping Cart (Sidebar/Modal)
- **Slide-in panel** from right (w-full max-w-md)
- **Cart Items**: Image thumbnail + details + quantity controls
- **Subtotal**: Clear pricing breakdown
- **CTAs**: "Continue Shopping" + "Checkout" (prominent)

### Buttons
- **Primary**: Solid, rounded-lg, px-6 py-3, font-medium
- **Secondary**: Outlined or ghost style
- **Icon Buttons**: rounded-full, p-2 or p-3
- **Sizes**: Small (py-2 px-4), Medium (py-3 px-6), Large (py-4 px-8)

### Input Fields
- **Style**: Consistent border, rounded-md, px-4 py-2.5
- **Focus states**: Ring-2 with offset
- **Labels**: text-sm font-medium, mb-2
- **Search bar**: Large, prominent with search icon

### Badges & Tags
- **Style**: Rounded-full or rounded-md, px-3 py-1, text-xs font-medium
- **Usage**: Product status, category tags, notifications

---

## Images

### Product Images
- **Critical Requirement**: Each product MUST have a unique, high-quality image
- **Image Sources**: Use royalty-free image services (Unsplash, Pexels) with diverse product photography
- **Variety**: Ensure visual diversity across products - different angles, contexts, and compositions
- **Format**: Modern formats (WebP with JPG fallback)
- **Lazy Loading**: Implement for performance

### Hero Section
- **Large hero image**: Full-width, high-impact lifestyle or product photography
- **Overlay**: Gradient overlay for text readability
- **Image description**: E-commerce lifestyle scene showing products in use or aspirational setting

### Category Images
- **Representative images** for each category showing key products or lifestyle context
- **Consistent aspect ratio** across all category cards

---

## Animations

**Use Sparingly**:
- Product card hover: scale-105 transition (200-300ms)
- Button hover: subtle opacity or shadow change
- Cart badge: Pulse animation on item add
- **Avoid**: Complex scroll animations, unnecessary transitions

---

## Accessibility

- **Image alt text**: Descriptive alt text for all product images
- **Keyboard navigation**: Full support for tab navigation
- **ARIA labels**: Proper labeling for buttons, inputs, and interactive elements
- **Focus indicators**: Clear, visible focus states
- **Contrast ratios**: Ensure WCAG AA compliance for text

---

## Icon Library

**Font Awesome** (via CDN) for comprehensive icon coverage:
- Shopping cart, search, user account
- Star ratings, wishlist heart
- Social media icons
- Navigation arrows, close icons